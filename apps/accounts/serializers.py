from rest_framework import serializers
from django.db import transaction
from apps.accounts.models import User, Organization, Membership


class SignupSerializer(serializers.ModelSerializer):

    organization = serializers.CharField(max_length=30, write_only=True)

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password", "organization"]

    def create(self, validated_objects):

        organization_name = validated_objects.pop("organization")
        password = validated_objects.pop("password")

        with transaction.atomic():
            user = User.objects.create_user(
                email=validated_objects["email"],
                password=password,
            )

            organization = Organization.objects.create(
                name=organization_name,
            )

            Membership.objects.create(
                user=user,
                organization=organization,
                role=Membership.Role.ADMIN,
            )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]
        read_only_fields = [
            "id",
            "email",
        ]
