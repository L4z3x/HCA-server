from rest_framework import serializers
from .models import ContactUs, ReportIssue, ReportComment


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
    class Meta:
        model = ReportComment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and not request.user.has_perm("blog.permissions.IsAdmin"):
            self.fields["status"].read_only = True
