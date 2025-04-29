from rest_framework.serializers import ModelSerializer
from user.models import user


class UserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = [
            "id",
            "username",
            "password",
            "email",
            "score",
            "profilePic",
            "role",
            "departement",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"read_only": True, "required": False},
            "password": {"write_only": True, "required": False},
            "username": {"required": False},
        }
