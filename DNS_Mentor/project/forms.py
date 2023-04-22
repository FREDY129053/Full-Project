from django import forms
from .models import Mentor


class MentorForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    telegram = forms.CharField(max_length=30)
    profession = forms.Textarea()
    about_me = forms.Textarea()
