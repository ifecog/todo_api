from django.shortcuts import render
from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        todos = Todo.objects.filter(
            user=user, date_completed__isnull=True).order_by('-date_completed')

        return todos

    def create(self, request, *args, **kwargs):
        data = request.data
        todo = Todo.objects.create(
            title=data['title'], crucial=data['crucial'], memo=data['memo'])

        todo.save()

        serializer = TodoSerializer(todo)
        return Response(serializer.data)
