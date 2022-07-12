from django import forms
from .models import URLShortenerModel


class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortenerModel
        fields = ('url',)
