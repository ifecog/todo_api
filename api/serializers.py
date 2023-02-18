from rest_framework import serializers
from todo.models import Todo

# Serializers define the API representation.


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'crucial', 'memo',
                  'date_created', 'date_completed')
        read_only_fields = ['date_created', 'date_completed']
