from rest_framework.serializers import ModelSerializer
from user.models import user


class UserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ["id", "username", "email", "score", "profilePic"]
        extra_kwargs = {"id": {"read_only": True}, "email": {"read_only": True}}
