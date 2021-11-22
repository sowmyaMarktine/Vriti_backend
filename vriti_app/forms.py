# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms 
from captcha.fields import CaptchaField


CHOICES = [
    ('employer', 'Employer'),
    ('employee', 'Employee'),
]

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required = True)
    category = forms.CharField(max_length = 100, label = 'Select Category', widget=forms.Select(choices=CHOICES))
    captcha = CaptchaField()
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'category']
