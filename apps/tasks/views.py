from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import HasActiveOrganization, IsOrgAdmin

from .models import Task
from .serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, HasActiveOrganization]

    def get_permissions(self):
        if self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                HasActiveOrganization,
                IsOrgAdmin,
            ]
        else:
            permission_classes = [
                IsAuthenticated,
                HasActiveOrganization,
            ]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        return Task.objects.filter(organization=self.request.active_organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.active_organization)
