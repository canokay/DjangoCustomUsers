from django import forms
from CustomUsers.models import UserStatus


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Username",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus'}))
    confirm = forms.CharField(max_length=20, label="Parolayı Doğrulayın", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'rpassword', 'id': 'rpassword', 'onkeyup': 'checkPass()', 'return': 'false', 'required': 'required', 'autofocus': 'autofocus'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parola Eşleşmedi :(")

        values = {
            "username": username,
            "password": password
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Kullanıcı Adı", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parola", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'name': 'password', 'id': 'password', 'required': 'required', 'autofocus': 'autofocus'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")


class UserStatusForm(forms.ModelForm):
    class Meta:
        model = UserStatus
        fields = ["userStatus"]
