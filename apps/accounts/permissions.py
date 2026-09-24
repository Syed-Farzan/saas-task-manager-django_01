from rest_framework.permissions import BasePermission
from rest_framework.exceptions import ValidationError
import uuid
from apps.accounts.models import Membership


class HasActiveOrganization(BasePermission):

    def has_permission(self, request, views):

        org_id = request.headers.get("X-Organization-Id")

        if not org_id:
            raise ValidationError({"detail": "X-Organization-Id header is required."})

        try:
            uuid.UUID(org_id)
        except ValueError:
            raise ValidationError({"detail": "Invalid organization ID."})

        membership = (
            Membership.objects.select_related("organization")
            .filter(user=request.user, organization=org_id)
            .first()
        )

        if not membership:
            return False

        request.active_organization = membership.organization
        request.membership = membership

        return True
