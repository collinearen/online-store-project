from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from users.models import User
from users.tasks import send_email_verification


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4",
        "placeholder": "Введите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4", "placeholder": "Имя"}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Фамилия"}))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Имя пользователя"}))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Введите ваш e-mail"}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Ваш пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        "placeholder": "Повторный ввод пароля"}))

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=True)
        send_email_verification.delay(user.id)
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4", 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control py-4", 'readonly': True}))

    class Meta:
        model = User
        fields = ("image", "first_name", 'last_name', 'username', 'email')
