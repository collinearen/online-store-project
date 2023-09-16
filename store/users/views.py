from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm
    name_store = 'Coffee Like'


class UserRegisterView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    name_store = 'Coffee Like'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'
    name_store = 'Coffee Like'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id))


class EmailVerificationView(TitleMixin, TemplateView):
    name_store = "Подтверждение e-mail"
    template_name = 'email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
