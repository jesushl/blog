from django import forms
from blog.models import Image

class ImageForm(forms.ModelForm):
   class Meta:
      model = Image
      fields = ['image','name']