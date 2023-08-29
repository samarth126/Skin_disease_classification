from django import forms
from .models import *

class img_form(forms.Form):
    disease_image = forms.ImageField()
    class Meta:
       model = img_check