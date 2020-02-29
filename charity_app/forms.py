from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, validate_email
from django.forms import CheckboxSelectMultiple

from charity_app.models import TYPE, Category, Institution, Donation, User


class RegisterForm(forms.ModelForm):

    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password")
        model = User
        widgets = {"password": forms.PasswordInput}
        validators = {"email": [validate_email]}


class LoginForm(forms.Form):
    email = forms.CharField(max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)
