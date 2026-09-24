from rest_framework import serializers

from apps.accounts.models import User


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

    def create(self, validated_objects):
        return User.objects.create_user(
            email=validated_objects["email"], password=validated_objects["password"]
        )


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
