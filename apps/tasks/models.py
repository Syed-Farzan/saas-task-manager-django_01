from django.db import models
from apps.accounts.models import Organization
from django.conf import settings


class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=30, default=Status.PENDING, choices=Status.choices
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
