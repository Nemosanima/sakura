from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def login_system(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('products:index')
    else:
        messages.success(request, 'Убедитесь, что введеные данные верны.')
        return redirect('users:login')


def logout_system(request):
    logout(request)
    return redirect('products:index')


def signup_system(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('products:index')
    else:
        return render(request, 'users/signup.html', {'form': form})

