from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        if email:
            user = self.model(email=email, **kwargs)
            user.set_password(password)
            user.save()
            return user
        else:
            raise ValueError("wrong email")

    def create_superuser(self, email, password=None, **kwargs):
        kwargs["is_staff"] = True
        kwargs["is_superuser"] = True
        email = self.normalize_email(email)
        if email:
            user = self.model(email=email, **kwargs)
            user.set_password(password)
            user.save()
            return user
        else:
            raise ValueError("wrong email")


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(unique=True)
    username = None
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Organization(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Membership(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        MEMBER = "member", "Member"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, default=Role.MEMBER, choices=Role.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "organization"], name="unique_membership_per_org"
            )
        ]
