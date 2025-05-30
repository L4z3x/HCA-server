from django.contrib import admin
from feedback.models import ContactUs, ReportIssue, ReportComment


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "status", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at", "status")
    ordering = ("-created_at",)


@admin.register(ReportIssue)
class ReportIssueAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "reported_by", "created_at", "status")
    search_fields = ("title", "reported_by")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)


@admin.register(ReportComment)
class ReportCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "comment", "status", "reported_by", "created_at")
    search_fields = ("comment__content", "reported_by")
    list_filter = ("created_at", "status")
    ordering = ("-created_at",)
