from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    crucial = models.BooleanField(default=False)
    memo = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    date_created = models.DateTimeField(
        default=datetime.now, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
