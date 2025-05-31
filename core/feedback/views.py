from rest_framework import generics
from .models import ContactUs, ReportIssue, ReportComment
from .serializers import (
    ContactUsSerializer,
    ReportIssueSerializer,
    ReportCommentSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
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
    permission_classes = [AllowAny]
    throttle_classes = [CustomAnonThrottle]


class ReportCommentCreateView(generics.CreateAPIView):
    queryset = ReportComment.objects.all()
    serializer_class = ReportCommentSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [CustomAnonThrottle]

    def post(self, request, *args, **kwargs):
        reported_by = {
            "username": request.user.username,
            "id": request.user.id,
            "profilePic": request.user.profilePic.url
            if request.user.profilePic
            else None,
        }
        print(reported_by)
        request.data["reported_by"] = reported_by
        return super().post(request, *args, **kwargs)


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
