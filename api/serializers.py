from rest_framework import serializers
from todo.models import Todo

# Serializers define the API representation.


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('user', 'title', 'crucial', 'memo',
                  'date_cvreated', 'date_completed')
        read_only_fields = ['date_created', 'days_completed']
