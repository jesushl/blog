from django import forms
from blog.models import Image, Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "message"]
