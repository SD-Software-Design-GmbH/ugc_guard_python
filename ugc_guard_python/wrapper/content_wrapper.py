import enum
import json
from typing import Optional, List, Union
from datetime import datetime


class ContentType(enum.Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    OTHER = "other"


class Body:
    def __init__(self, content_type: ContentType, body: Union[str, List["MultiMediaBody"]]) -> None:
        if self.__class__ == Body:
            raise TypeError("Abstract classes can't be instantiated.")
        self.content_type = content_type
        self.body = body



class JsonBody(Body):
    """
    JsonBody is used to represent JSON content in a report.
    """
    def __init__(self, json_data: dict) -> None:
        super().__init__(content_type=ContentType.OTHER, body=json.dumps(json_data))
        self.json_data = json_data



class TextBody(Body):
    """
    TextBody is used to represent plain text content in a report.
    """
    def __init__(self, text: str) -> None:
        super().__init__(content_type=ContentType.TEXT, body=text)
        self.text = text


class ProxiedMultiMultiMediaBody(Body):
    """
    Proxied MultiMultiMediaBody is used to represent media that is proxied through URLS.
    See https://docs.ugc-guard.com/docs/getting-started/files.html#_2-proxying-media
    """

    def __init__(self, content_type: ContentType, urls: list[str], body: str = "") -> None:
        super().__init__(content_type=content_type, body=body)
        self.urls = urls


class MultiMediaBody(Body):
    """
    MultiMediaBody is used to represent media files that are uploaded directly.

    See https://docs.ugc-guard.com/docs/getting-started/files.html#_1-uploading-files-to-ugc-guard
    """

    def __init__(
            self,
            bytes_: bytes,
            filename: str,
            mime_type: str,
            content_type: Optional[ContentType] = None,
            body: str = ""
    ) -> None:
        content_type = content_type or self._detect_content_type(mime_type)
        super().__init__(content_type=content_type, body=body)
        self.bytes = bytes_
        self.filename = filename
        self.mime_type = mime_type

    @staticmethod
    def _detect_content_type(mime_type: str) -> ContentType:
        if mime_type.startswith("image/"):
            return ContentType.IMAGE
        elif mime_type.startswith("video/"):
            return ContentType.VIDEO
        elif mime_type.startswith("audio/"):
            return ContentType.AUDIO
        return ContentType.FILE


class MultiMultiMediaBody(Body):
    """
    MultiMultiMediaBody is used to represent multiple media files that are uploaded directly.
    """
    def __init__(self, media: List[MultiMediaBody], content_type: ContentType = ContentType.IMAGE) -> None:
        super().__init__(content_type=content_type, body=media)
        self.media = media


class ReportContent:
    """
    Actual content of a report, which can be the "main content" or "context content".

    The body of this content can be a [TextBody], [MultiMediaBody], [MultiMultiMediaBody] or [ProxiedMultiMultiMediaBody].
    """

    def __init__(
            self,
            unique_partner_id: str,
            body: Union[TextBody, MultiMediaBody, MultiMultiMediaBody, ProxiedMultiMultiMediaBody],
            additional_data: Optional[dict] = None,
            ip: Optional[str] = None,
            created_at: Optional[datetime] = None
    ) -> None:
        self.unique_partner_id = unique_partner_id
        self.body = body
        self.additional_data = additional_data
        self.ip = ip
        self.created_at = created_at


class ReportPerson:
    """
    A person who reported content or who created content in a report.

    Media_identifiers are the profile pictures of the person. They can be as always either URLs or the IDs of files
    uploaded to UGC Guard. They must be images.

    You can add files to be uploaded later with the add_file_name method. The file will be uploaded to UGC Guard and
    then its ID will be added to the media_identifiers list.
    """

    file_names: List[str] = []

    def __init__(
            self,
            unique_partner_id: str,
            name: Optional[str] = None,
            email: Optional[str] = None,
            phone: Optional[str] = None,
            additional_data: Optional[dict] = None,
            media_identifiers: Optional[List[str]] = None
    ) -> None:
        self.unique_partner_id = unique_partner_id
        self.name = name
        self.email = email
        self.phone = phone
        self.additional_data = additional_data
        self.media_identifiers = media_identifiers

    def add_file_name(self, file_name: str) -> None:
        """
        Adds a file name to the list of file names associated with this person.

        The file will be uploaded to UGC Guard and then its ID will be added to the media_identifiers list.

        :param file_name: The name of the file to add.
        :return: None
        """
        self.file_names.append(file_name)



class ContentWrapper:
    """
    Wraps the actual content and creator information for a content object of a report.

    Creator can be None if the content was created by an anonymous user/by the system or by no known user.
    But please be aware that no creator means that your reviewers are missing important context about the content and
    some features of UGC Guard might not work as expected (e.g. related reports).
    """

    def __init__(self, content: ReportContent, creator: Optional[ReportPerson]) -> None:
        self.content = content
        self.creator = creator
