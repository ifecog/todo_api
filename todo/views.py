from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'pages/home.html')


def signup(request):
    context = {
        'form': UserCreationForm(),
        'usernameerror': 'Username already taken. Please, choose another',
        'passworderror': 'Passwords do not match. Try again!'
    }

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username, password=password)
                auth.login(request, user)
                user.save()
                return redirect(home)
            except IntegrityError:
                return render(request, 'accounts/signup.html', context)

    return render(request, 'accounts/signup.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return render(request, 'accounts/signin.html')
