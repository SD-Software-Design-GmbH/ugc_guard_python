import hashlib
import hmac
import ugc_guard_python
import json

from ugc_guard_python import ReportCategory
from ugc_guard_python.wrapper.content_wrapper import ContentWrapper, ReportContent, ReportPerson, Body, TextBody, \
    MultiMediaBody, MultiMultiMediaBody, ContentType
from typing import Optional, List, Dict, Any
from ugc_guard_python.models.body_create_magic_report import BodyCreateMagicReport
from ugc_guard_python.models.report_create import ReportCreate
from ugc_guard_python.models.reporter import Reporter
from ugc_guard_python.models.content_create import ContentCreate
from ugc_guard_python.models.main_content_sender import MainContentSender
from ugc_guard_python.models.person import Person
from ugc_guard_python.models.person_db import PersonDB


class GuardClient:

    def __init__(self, organization_id: str, base_url: str = "https://api.ugc-guard.com/") -> None:
        self.base_url = base_url.rstrip('/')
        self.organization_id = organization_id
        configuration = ugc_guard_python.Configuration(host=self.base_url)
        self.api_client = ugc_guard_python.ApiClient(configuration)

    @staticmethod
    def verify_signature(payload_body: dict, secret_token: str, signature_header: str) -> bool:
        """Verify that the payload was sent from UGC Guard by validating SHA256.

        Args:
            payload_body: original request body to verify (request.body())
            secret_token: UGC Guard webhook token (WEBHOOK_SECRET)
            signature_header: header received from UGC Guard (x-action-signature)

        returns:
            bool: True if the signature is valid else False.
        """
        if not signature_header:
            return False
        hash_object = hmac.new(secret_token.encode('utf-8'),
                               msg=json.dumps(payload_body, sort_keys=True).encode("utf-8"), digestmod=hashlib.sha256)
        expected_signature = "sha256=" + hash_object.hexdigest()
        if not hmac.compare_digest(expected_signature, signature_header):
            return False

        return True

    def report(
            self,
            module_id: str,
            module_secret: str,
            type_id: str,
            main_content: ContentWrapper,
            reporter: ReportPerson,
            description: Optional[str] = "",
            report_category: ReportCategory = ReportCategory.OTHER,
            user_message: Optional[str] = "",
            context: Optional[List[ContentWrapper]] = None,
            on_progress: Optional[callable] = None,
            channels: Optional[List[str]] = None,
    ) -> Any:
        """
        Creates a report with the given main content and context.

        Args:
            module_id (str): The ID of the module.
            module_secret (str): The secret for the module.
            type_id (str): The type ID of the report.
            main_content (ContentWrapper): The main content to be reported.
            reporter (ReportPerson): The person reporting the content.
            description (Optional[str]): Description of the report.
            report_category (ReportCategory): Category of the report.
            user_message (Optional[str]): Custom message from the user.
            context (Optional[List[ContentWrapper]]): Additional context for the report.
            on_progress (Optional[callable]): Callback function to track progress.
            channels (Optional[List[str]]): Channels to send the report to.
        """

        try:
            total_steps = len(context) + 2

            main_content_create = self.convert_content_to_content_create(
                main_content, module_id, module_secret
            )

            if on_progress:
                on_progress(1, total_steps)

            main_content_sender = self.convert_person_to_person_db(
                main_content.creator, module_id
            )

            report_context = []
            report_context_persons = []
            for i, content_wrapper in enumerate(context, start=2):
                content_create = self.convert_content_to_content_create(
                    content_wrapper, module_id, module_secret
                )
                if on_progress:
                    on_progress(i, total_steps)
                report_context.append(content_create)
                report_context_persons.append(
                    self.convert_person_to_person_db(content_wrapper.creator, module_id)
                )

            reporter_person = self.convert_person_to_person_db(reporter, module_id)
            reporter = Reporter(actual_instance=reporter_person)

            tmp = PersonDB(**main_content_sender.model_dump())

            main_content_sender = MainContentSender(actual_instance=tmp)
            report = ReportCreate(
                module_id=module_id,
                type_id=type_id,
                description=description
            )
            request_body = BodyCreateMagicReport(
                report=report,
                reporter=reporter,
                main_content=main_content_create,
                main_content_sender=main_content_sender,
                report_context=report_context,
                report_context_persons=report_context_persons,
                channels=channels
            )

            params = {
                "report_category": report_category,
                "secret": module_secret,
                "custom_message": user_message
            }

            reports_api = ugc_guard_python.ReportsApi(self.api_client)
            response = reports_api.create_magic_report(
                body_create_magic_report=request_body, **params
            )

            if on_progress:
                on_progress(total_steps, total_steps)

            return response
        except ugc_guard_python.ApiException as e:
            raise Exception(f"Exception when calling ReportsApi->create_magic_report: {e}")

    def convert_person_to_person_db(self, person: ReportPerson, module_id: str) -> Person:
        return Person(
            id=None,
            unique_partner_id=person.unique_partner_id,
            name=person.name,
            phone=person.phone,
            email=person.email,
            extra_data=person.additional_data,
            module_id=module_id
        )

    def convert_content_to_content_create(
            self, content_wrapper: ContentWrapper, module_id: str, module_secret: str
    ) -> ContentCreate:
        report_content = content_wrapper.content
        body = report_content.body
        type_ = body.content_type

        if type_ in [ContentType.OTHER, ContentType.TEXT]:
            return ContentCreate(
                creator_id=content_wrapper.creator.unique_partner_id,
                body=body.body,
                body_type=type_,
                created_at=report_content.created_at,
                extra_data=report_content.additional_data,
                ip=report_content.ip,
                unique_partner_id=report_content.unique_partner_id
            )
        else:
            media_identifiers = []
            if hasattr(body, 'urls') and not hasattr(body, 'bytes'):
                # Proxied content, no need to upload files
                media_identifiers = body.urls
            else:
                files = self.upload_files(module_id, module_secret, content_wrapper)
                if not files:
                    raise Exception("Failed to upload files.")
                media_identifiers = [f.id for f in files if f.id]

            if not media_identifiers:
                raise Exception("No media identifiers found after upload.")

            return ContentCreate(
                creator_id=content_wrapper.creator.unique_partner_id,
                body=body.body,
                body_type=body.content_type,
                created_at=report_content.created_at,
                extra_data=report_content.additional_data,
                ip=report_content.ip,
                unique_partner_id=report_content.unique_partner_id,
                media_identifiers=media_identifiers
            )

    def upload_files(
            self, module_id: str, module_secret: str, content: ContentWrapper
    ) -> list:
        """
        Uploads files from the content to the UGC Guard service.
        """
        body = content.content.body
        if body.content_type in [ContentType.OTHER, ContentType.TEXT]:
            raise Exception("Content must be of type MultiMediaBody to upload a file.")

        if self.is_multi_media_body(body):
            try:
                file = self._actual_upload(module_id, module_secret, body)
                return [file]
            except ugc_guard_python.ApiException as e:
                raise Exception(f"Exception when calling FilesApi->upload_file: {e}")
        elif self.is_multi_multi_media_body(body):
            results = []
            for multi_media_body in body.media:
                try:
                    file = self._actual_upload(module_id, module_secret, multi_media_body)
                    results.append(file)
                except ugc_guard_python.ApiException as e:
                    raise Exception(f"Exception when calling FilesApi->upload_file: {e}")
            return results
        return []

    def _actual_upload(
            self, module_id: str, module_secret: str, multi_media_body: MultiMediaBody
    ) -> Any:
        files_api = ugc_guard_python.FilesApi(self.api_client)
        return files_api.upload_file(
            module_id=module_id,
            upload_file=(multi_media_body.filename, multi_media_body.bytes),
            secret=module_secret
        )

    @staticmethod
    def is_multi_media_body(body: Body) -> bool:
        return isinstance(body, MultiMediaBody)

    @staticmethod
    def is_multi_multi_media_body(body: Body) -> bool:
        return isinstance(body, MultiMultiMediaBody)
