from django import forms
from .models import Categories


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="カテゴリー名",
        required=True,
    )

    class Meta:
        model = Categories
        fields = ('name',)
