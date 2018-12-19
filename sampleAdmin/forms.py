from django import forms
from sample.models import Blogs


class BlogForm(forms.ModelForm):
    content = forms.CharField(
        label="内容",
        required=True,
        widget=forms.Textarea
    )

    class Meta:
        model = Blogs
        fields = ('title', 'content',)
