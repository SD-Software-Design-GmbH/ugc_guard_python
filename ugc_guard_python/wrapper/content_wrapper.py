from typing import Optional, List, Union
from datetime import datetime

class ContentType:
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    OTHER = "other"


class Body:
    def __init__(self, content_type: str, body: Union[str, List["MultiMediaBody"]]) -> None:
        if self.__class__ == Body:
            raise TypeError("Abstract classes can't be instantiated.")
        self.content_type = content_type
        self.body = body


class TextBody(Body):
    def __init__(self, text: str) -> None:
        super().__init__(content_type=ContentType.TEXT, body=text)
        self.text = text


class MultiMediaBody(Body):
    def __init__(
        self,
        bytes_: bytes,
        filename: str,
        mime_type: str,
        content_type: Optional[str] = None,
        body: str = ""
    ) -> None:
        content_type = content_type or self._detect_content_type(mime_type)
        super().__init__(content_type=content_type, body=body)
        self.bytes = bytes_
        self.filename = filename
        self.mime_type = mime_type

    @staticmethod
    def _detect_content_type(mime_type: str) -> str:
        if mime_type.startswith("image/"):
            return ContentType.IMAGE
        elif mime_type.startswith("video/"):
            return ContentType.VIDEO
        elif mime_type.startswith("audio/"):
            return ContentType.AUDIO
        return ContentType.FILE


class MultiMultiMediaBody(Body):
    def __init__(self, media: List[MultiMediaBody], content_type: str = ContentType.IMAGE) -> None:
        super().__init__(content_type=content_type, body=media)
        self.media = media


class ReportContent:
    def __init__(
        self,
        unique_partner_id: str,
        body: Union[TextBody, MultiMediaBody, MultiMultiMediaBody],
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
    def __init__(
        self,
        unique_partner_id: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        additional_data: Optional[dict] = None
    ) -> None:
        self.unique_partner_id = unique_partner_id
        self.name = name
        self.email = email
        self.phone = phone
        self.additional_data = additional_data


class ContentWrapper:
    def __init__(self, content: ReportContent, creator: ReportPerson) -> None:
        self.content = content
        self.creator = creator