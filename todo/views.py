from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
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
            return redirect(signin)

    return render(request, 'accounts/signin.html')


@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)


@login_required
def create_todo(request):
    context = {
        'form': TodoForm(),
        'error': 'Bad data passed in. Try again.',
    }
    try:
        form = TodoForm(request.POST)
        new_todo = form.save(commit=False)
        new_todo.user = request.user
        new_todo.save()
        return redirect(current_todos)
    except ValueError:
        return render(request, 'pages/createtodo.html', context)


@login_required
def current_todos(request):
    todos = Todo.objects.filter(
        user=request.user, date_completed__isnull=True)
    context = {
        'todos': todos,
    }

    return render(request, 'pages/currenttodos.html', context)


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(
        user=request.user, date_completed__isnull=False).order_by('-date_created')
    context = {
        'todos': todos,
    }

    return render(request, 'pages/completedtodos.html', context)


@login_required
def todo_detail(request, todo_slug):
    single_todo = get_object_or_404(Todo, slug=todo_slug, user=request.user)
    form = TodoForm(instance=single_todo)

    context = {
        'todo': single_todo,
        'form': form,
        'error': 'Bad Info',
    }

    try:
        form = TodoForm(request.POST, instance=single_todo)
        form.save()
        return redirect(current_todos)
    except ValueError:
        return render(request, 'pages/tododetail.html', context)


@login_required
def complete_todo(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect(current_todos)


def delete_todo(request, todo_slug):
    todo = get_object_or_404(Todo, slug=todo_slug, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect(current_todos)
