from django import forms
from blog.models import Image


class ImageForm(forms.ModelForm):

    class Meta:

        model = Image
        fields = ['image', ' name']


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100
    )
    email = forms.EmailField()
    message = forms.CharField(
        label="Message",
        max_length=1500
    )
