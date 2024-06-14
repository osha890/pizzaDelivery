from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pizza_list')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'title': 'Sign up'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pizza_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'title': 'Log in'})


def logout_view(request):
    logout(request)
    return redirect('login')
