from rest_framework.serializers import ModelSerializer, ImageField
from user.models import user
from core.utils import upload_image


class UserSerializer(ModelSerializer):
    profilePicFile = ImageField(write_only=True, required=False)

    class Meta:
        model = user
        fields = [
            "id",
            "username",
            "password",
            "email",
            "score",
            "profilePic",
            "profilePicFile",
            "role",
            "departement",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"required": False},
            "password": {"write_only": True, "required": False},
            "username": {"required": False},
            "profilePic": {"read_only": True},
        }

    def update(self, instance, validated_data):
        image = validated_data.get("profilePicFile", None)
        if image:
            filename = f"{instance.username}_{instance.id}"
            file = upload_image(image, filename, folder="profile-pics")
            validated_data["profilePic"] = file["secure_url"]
        return super().update(instance, validated_data)
