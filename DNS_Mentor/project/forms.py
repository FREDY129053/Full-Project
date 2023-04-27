from django import forms
from .models import Mentor


class MentorForm(forms.Form):
    # model = Mentor()
    first_name = forms.CharField(widget=forms.Textarea)
    last_name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    telegram = forms.CharField(widget=forms.Textarea)
    price = forms.CharField(widget=forms.Textarea)
    exp = forms.CharField(widget=forms.Textarea)
    profession = forms.CharField(widget=forms.Textarea)
    about_me = forms.CharField(widget=forms.Textarea)


class UserForm(forms.Form):
    user_name = forms.CharField(widget=forms.Textarea)
    user_surname = forms.CharField(widget=forms.Textarea)
    user_email = forms.EmailField()
    user_telegram = forms.CharField(widget=forms.Textarea)
    meeting_date = forms.DateField()
    mentor_tg = forms.CharField(widget=forms.Textarea)
