from django import forms
from blog.models import Image


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100
    )
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
