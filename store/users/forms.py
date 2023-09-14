from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


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