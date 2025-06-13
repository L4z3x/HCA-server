from rest_framework.serializers import ModelSerializer, ImageField
from user.models import user
from core.utils import upload_to_drive
from core.settings import PROFILE_PIC_FOLDER_ID


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
        print(image)

        if image:
            filename = f"{instance.id}.{image.name.split('.')[-1]}"
            if not filename:
                filename = f"{instance.id}.jpg"
            file = upload_to_drive(image, filename, PROFILE_PIC_FOLDER_ID)
            validated_data["profilePic"] = (
                f"https://drive.google.com/uc?export=view&id={file['id']}"
            )
        print(validated_data["profilePic"])
        return super().update(instance, validated_data)
