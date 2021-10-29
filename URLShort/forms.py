from django.forms import fields
from django import forms 


class ShortRequestForm(forms.Form):
    url = forms.URLField(max_length=200)