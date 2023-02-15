from django.contrib import admin
from .models import Todo

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('id', 'user', 'title', 'crucial')
    list_display_links = ('user', 'title')
    search_fields = ('user', 'title')
