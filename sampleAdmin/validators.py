import magic
from django.core.exceptions import ValidationError


class MimeTypeValidator:

    def __init__(self, allowed_mime_types):
        self.allowed_mime_types = allowed_mime_types

    def __call__(self, value):
        mime_type = magic.from_buffer(value.read(1024), mime=True)
        if mime_type not in self.allowed_mime_types:
            raise ValidationError("ファイルの種類を確認してください")
