from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm, UserLoginForm


def register_user(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login-view')

    user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in')
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(f'Authenticated as {username}')
            else:
                return HttpResponse('Invalid login')

    login_form = UserLoginForm()
    return render(request, 'users/login.html', {'login_form': login_form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse('Logged out')
