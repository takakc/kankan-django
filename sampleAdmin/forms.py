from django import forms
from sample.models import Blogs
from .validators import MimeTypeValidator

ALLOWED_MIME_TYPES = [
    'image/jpeg',
    'image/png',
]


class BlogForm(forms.ModelForm):
    content = forms.CharField(
        label="内容",
        required=True,
        widget=forms.Textarea
    )

    image = forms.ImageField(
        label="画像",
        required=False,
    )

    class Meta:
        model = Blogs
        fields = ('title', 'content', 'image', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].validators = [
            MimeTypeValidator(ALLOWED_MIME_TYPES)
        ]
