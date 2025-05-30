from rest_framework import generics
from .models import ContactUs, ReportIssue, ReportComment
from .serializers import (
    ContactUsSerializer,
    ReportIssueSerializer,
    ReportCommentSerializer,
)
from rest_framework.permissions import AllowAny
from blog.permissions import IsAdmin
from feedback.throttling import CustomAnonThrottle
# --- user views -----


class ContactUsCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    throttle_classes = [CustomAnonThrottle]


class ReportIssueCreateView(generics.CreateAPIView):
    queryset = ReportIssue.objects.all()
    serializer_class = ReportIssueSerializer
    throttle_classes = [CustomAnonThrottle]


class ReportCommentCreateView(generics.CreateAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer
    throttle_classes = [CustomAnonThrottle]


# --- admin views -----

# ---> list views


class ContactUsListView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAdmin]


class ReportIssueListView(generics.ListAPIView):
    queryset = ReportIssue.objects.all()
    serializer_class = ReportIssueSerializer
    permission_classes = [IsAdmin]


class ReportCommentListView(generics.ListAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer
    permission_classes = [IsAdmin]


# ---> detail views


class ContactUsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAdmin]


class ReportCommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer
    permission_classes = [IsAdmin]


class ReportIssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportIssue.objects.all()
    serializer_class = ReportIssueSerializer
    permission_classes = [IsAdmin]
