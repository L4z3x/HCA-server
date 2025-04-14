from rest_framework.serializers import ModelSerializer
from .models import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "body",
            "author",
            "created_at",
            "updated_at",
            "thumbnail",
        ]
        read_only_fields = ["id", "author", "created_at", "updated_at"]
        extra_kwargs = {
            "title": {"required": True},
            "body": {"required": True},
            "thumbnail": {"required": False},
        }


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "author", "thumbnail", "created_at", "updated_at"]
        read_only_fields = ["author", "created_at", "updated_at"]
        required_fields = ["title"]
        # extra_kwargs = {
        #     "title": {"required": True},
        # }
