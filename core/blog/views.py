from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.permissions import IsWriter

from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])  # , IsWriter
def create_blog(request):
    user = request.user
    if not user:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = BlogSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save(author=user)
    return Response(status=status.HTTP_201_CREATED)
