from django.urls import path
from feedback.views import (
    ContactUsCreateView,
    ContactUsDetailView,
    ContactUsListView,
    ReportCommentCreateView,
    ReportCommentDetailView,
    ReportCommentListView,
    ReportIssueCreateView,
    ReportIssueListView,
    ReportIssueDetailView,
)

urlpatterns = [
    # User views
    path("contact-us/", ContactUsCreateView.as_view(), name="contact-us-create"),
    path("report-issue/", ReportIssueCreateView.as_view(), name="report-issue-create"),
    path(
        "report-comment/",
        ReportCommentCreateView.as_view(),
        name="report-comment-create",
    ),
    # Admin views
    path("admin/contact-us/", ContactUsListView.as_view(), name="contact-us-list"),
    path(
        "admin/report-issue/", ReportIssueListView.as_view(), name="report-issue-list"
    ),
    path(
        "admin/report-comment/",
        ReportCommentListView.as_view(),
        name="report-comment-list",
    ),
    # Detail views
    path(
        "admin/contact-us/<int:pk>/",
        ContactUsDetailView.as_view(),
        name="contact-us-detail",
    ),
    path(
        "admin/report-issue/<int:pk>/",
        ReportIssueDetailView.as_view(),
        name="report-issue-detail",
    ),
    path(
        "admin/report-comment/<int:pk>/",
        ReportCommentDetailView.as_view(),
        name="report-comment-detail",
    ),
]
