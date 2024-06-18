
from .models import Url
from django import forms


class UrlForm(forms.ModelForm):

    class Meta:

        model = Url
        fields = ["url"]
