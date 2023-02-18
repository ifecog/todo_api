from django.shortcuts import
from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        todos = Todo.objects.filter(
            user=user, date_completed__isnull=False).order_by('-date_completed')

        return todos
