from rest_framework.serializers import ModelSerializer, ImageField, IntegerField
from blog.models import Blog, Comment
from user.models import user
from rest_framework.response import Response
from core.utils import upload_image


class ShortUserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ["id", "username", "profilePic"]
        read_only_fields = ["id", "username", "profilePic"]


class BlogSerializer(ModelSerializer):
    like = IntegerField(source="likes.count", read_only=True)
    comment = IntegerField(source="comments.count", read_only=True)
    author = ShortUserSerializer(read_only=True)
    thumbnailFile = ImageField(write_only=True, required=False)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "like",
            "comment",
            "description",
            "body",
            "author",
            "created_at",
            "updated_at",
            "thumbnail",
            "thumbnailFile",
        ]
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "updated_at",
            "thumbnail",
        ]
        extra_kwargs = {
            "title": {"required": True},
            "body": {"required": True},
            "description": {"required": True},
            "thumbnailFile": {"required": True, "write_only": True},
            "thumbnail": {"read_only": True},
        }

    def update(self, instance, validated_data):
        image = validated_data.get("thumbnailFile", None)
        if image is not None:
            filename = f"{instance.title}"
            file = upload_image(image, filename, folder="blog-thumbnails")
            validated_data["thumbnail"] = file["secure_url"]
            validated_data.pop("thumbnailFile")
        return super().update(instance, validated_data)

    def create(self, validated_data):
        image = validated_data.get("thumbnailFile", None)
        if image:
            filename = f"{validated_data['title']}"
            file = upload_image(image, filename, folder="blog-thumbnails")
            validated_data["thumbnail"] = file["secure_url"]
            validated_data.pop("thumbnailFile")
            return super().create(validated_data)
        else:
            return Response({"error": "Thumbnail image is required."}, status=400)


class BlogListSerializer(ModelSerializer):
    like = IntegerField(source="likes.count", read_only=True)
    comment = IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "like",
            "comment",
            "title",
            "description",
            "author",
            "thumbnail",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author", "created_at", "updated_at"]
        required_fields = ["title"]
        # extra_kwargs = {
        #     "title": {"required": True},
        # }


class CommentSerializer(ModelSerializer):
    author = ShortUserSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "body",
            "blog",
            "author",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "body": {"required": True},
            "author": {"required": True},
        }

    def create(self, validated_data):
        author = self.context["request"].user
        validated_data["author"] = author
        return super().create(validated_data)
