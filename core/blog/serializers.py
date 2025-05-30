from rest_framework.serializers import ModelSerializer, CharField, IntegerField
from blog.models import Blog, Comment
from user.models import user


class ShortUserSerializer(ModelSerializer):
    class Meta:
        model = user
        fields = ["id", "username", "profilePic"]
        read_only_fields = ["id", "username", "profilePic"]


class BlogSerializer(ModelSerializer):
    like = IntegerField(source="likes.count", read_only=True)
    comment = IntegerField(source="comments.count", read_only=True)
    author = ShortUserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "like",
            "comment",
            "body",
            "author",
            "created_at",
            "updated_at",
            "thumbnail",
        ]
        read_only_fields = [
            "id",
            "author",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "title": {"required": True},
            "body": {"required": True},
            "thumbnail": {"required": False},
        }


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
    author = ShortUserSerializer(read_only=True)

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
            "author": {"required": False},
        }
