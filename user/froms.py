from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره همراه'})
    # )

    username = forms.CharField(
        label='شماره همراه',
        widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'شماره همراه'})
    )
    password = forms.CharField(
        label='رمز',
        widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'رمز عبور'})
    )