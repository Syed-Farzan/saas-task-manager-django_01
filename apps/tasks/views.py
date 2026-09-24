from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.accounts.permissions import HasActiveOrganization

from .models import Task
from .serializers import TaskSerializer


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, HasActiveOrganization]

    def get_queryset(self):
        return Task.objects.filter(organization=self.request.active_organization)

    def perform_create(self, serializer):
        serializer.save(organization=self.request.active_organization)
