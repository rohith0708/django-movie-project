from django import forms
from django.forms import fields

from .models import movie
class movie_form(forms.ModelForm):
     class Meta:
         model=movie
         fields=['name','desc','year','img']
