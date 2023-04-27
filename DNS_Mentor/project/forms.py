from django import forms
from .models import Mentor


class MentorForm(forms.Form):
    model = Mentor()
    first_name = forms.CharField(widget=forms.Textarea)
    last_name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    telegram = forms.CharField(widget=forms.Textarea)
    price = forms.CharField(widget=forms.Textarea)
    exp = forms.CharField(widget=forms.Textarea)
    profession = forms.CharField(widget=forms.Textarea)
    about_me = forms.CharField(widget=forms.Textarea)
