from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
class UserForm(forms.Form):
     name = forms.CharField()

class CustomUserLoginForm(forms.Form):
    attrs = {
        'placeholder': 'Пароль',
        "type": "password"
    }
    username = forms.CharField(label='Enter Username', widget=forms.TextInput(attrs={'placeholder': 'Логин'}), min_length=4, max_length=150)
    password = forms.CharField(label='Enter password',widget=forms.TextInput(attrs=attrs))
    def save(self, commit=True):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        return user

class CustomUserCreateForm(forms.Form):
    attrs_pass1 = {
        'placeholder': 'Пароль',
        "type": "password"
    }
    attrs_pass2 = {
        'placeholder': 'Еще раз',
        "type": "password"
    }
    username = forms.CharField(label='Enter Username', widget=forms.TextInput(attrs={'placeholder': 'Логин'}), min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email', widget=forms.TextInput(attrs={'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Enter password', widget=forms.TextInput(attrs=attrs_pass1))
    password2 = forms.CharField(label='Confirm password', widget=forms.TextInput(attrs=attrs_pass2))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Имя пользователя занято")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Аккаунт с такой почтой уже существует")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return password2
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user