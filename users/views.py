from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from users.forms import UserRegistrationForm, UserLoginForm


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login-view')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form})


def login_user(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated as', request.user)
            else:
                return HttpResponse('Invalid login')

    else:
        login_form = UserLoginForm()

    return render(request, 'users/login.html', {'login_form': login_form})
