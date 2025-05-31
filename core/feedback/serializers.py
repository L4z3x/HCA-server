from rest_framework import serializers
from .models import ContactUs, ReportIssue, ReportComment
from blog.serializers import ShortUserSerializer


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and not request.user.has_perm("blog.permissions.IsAdmin"):
            self.fields["status"].read_only = True


class ReportIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportIssue
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and not request.user.has_perm("blog.permissions.IsAdmin"):
            self.fields["status"].read_only = True


class ReportCommentSerializer(serializers.ModelSerializer):
    reported_by = ShortUserSerializer(read_only=True)
    comment_body = serializers.CharField(source="comment.body", read_only=True)

    class Meta:
        model = ReportComment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and not request.user.has_perm("blog.permissions.IsAdmin"):
            self.fields["status"].read_only = True

    def create(self, validated_data):
        reported_by = self.context["request"].user
        validated_data["reported_by"] = reported_by
        return super().create(validated_data)
