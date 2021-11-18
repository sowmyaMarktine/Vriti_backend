# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

CHOICES = [
    ('employer', 'Employer'),
    ('employee', 'Employee'),
]
class CreateUserForm(UserCreationForm):
    category = forms.CharField(max_length = 100, label = 'Select Category', widget=forms.Select(choices=CHOICES))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', "category"]