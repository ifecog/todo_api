from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('current_todos/', views.current_todos, name='current_todos'),
    path('<slug:todo_slug>/', views.todo_detail, name='todo_detail'),
    path('<slug:todo_slug>/complete/', views.complete_todo, name='complete'),
    path('<slug:todo_slug>/delete/', views.delete_todo, name='delete'),
]
