from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
        "user_id",
        "title",
        "details",
        "created_at",
        "reminder",
        "is_completed",
        ]