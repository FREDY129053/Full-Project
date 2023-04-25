from django import forms
from .models import Mentor


class MyForm(forms.Form):
    label_suffix = ""
    my_field = forms.MultipleChoiceField(choices=[('Data Science', 'Data Science'), ('Front-end', 'Front-end'), ('Backend', 'Backend')])


class MentorForm(forms.Form):
    model = Mentor()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    telegram = forms.CharField(max_length=30)
    profession = forms.Textarea()
    about_me = forms.Textarea()
