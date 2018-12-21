from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from djangocustomusersAbstract_app.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username: ")
    password = forms.CharField(
        max_length=50, label="Password: ", widget=forms.PasswordInput)
    confirm = forms.CharField(
        max_length=50, label="Password again: ", widget=forms.PasswordInput)
    status = forms.CharField(max_length=50, label="status: ")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        status = self.cleaned_data.get("status")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parola eşleşmedi")

        values = {
            "username": username,
            "password": password,
            "status": status,
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
