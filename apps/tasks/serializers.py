from rest_framework import serializers
from apps.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "id",
            "organization",
            "title",
            "description",
            "status",
            "assignee",
            "created_at",
            "due_date",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "organization",
            "created_at",
            "updated_at",
        ]
