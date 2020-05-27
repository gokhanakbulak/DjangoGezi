import self as self
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :'),
    email = forms.EmailField(max_length=30, label='E-mail :'),
    first_name = forms.CharField(max_length=30, label='First Name :'),
    last_name = forms.CharField(max_length=30,help_text='Last Name', label='Last Name :'),

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Adress'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'password1': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '}),
            'password2': PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
