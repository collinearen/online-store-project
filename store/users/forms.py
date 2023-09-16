import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.timezone import now

from users.models import EmailVerification, User


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
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
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
