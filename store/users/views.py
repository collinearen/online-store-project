from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from products.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request=request, template_name="login.html", context=context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Поздравляем, вы успешно зарегистрировались!")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request=request, template_name="register.html", context=context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = UserProfileForm(instance=request.user)
    context = {"name_store": 'Coffee Lake', "form": form, 'baskets': Basket.objects.filter(user=request.user)}
    return render(request=request, template_name='profile.html', context=context)


def logout(request):
    auth.logout(request=request)
    return HttpResponseRedirect(reverse('index'))
