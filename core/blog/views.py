from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.permissions import IsWriter
from rest_framework.response import Response
from core.settings import BASE_URL
from rest_framework import status
from blog.serializers import BlogSerializer, CommentSerializer, BlogListSerializer
from blog.models import Blog, Comment
from user.models import user
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView,
)
from rest_framework.pagination import PageNumberPagination


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


class BlogListView(ListAPIView):
    """
    List all blogs by recent first
    """

    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    page_size = 12  # default page size
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all().order_by("-created_at")

    def get(self, request):
        return self.list(request)


class GetBlogView(RetrieveAPIView):
    """
    Get blog by id
    """

    lookup_field = "id"
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(id=self.kwargs.get("id"))

    def get(self, request, *args, **kwargs):
        res = self.retrieve(request, *args, **kwargs)
        if res.status_code == 200:
            author_id = res.data["author"]
            author = user.objects.filter(id=author_id).first()
            if author:
                res.data["author"] = {
                    "id": author.id,
                    "username": author.username,
                    "profilePic": f"{BASE_URL}{author.profilePic.url}"
                    if author.profilePic
                    else None,
                }
            else:
                res.data["author"] = None
            res.data["author_username"] = res.data["author"].get("username")
        return res


class BlogView(UpdateAPIView, DestroyAPIView):
    # permission_classes = [IsWriter]
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Blog.objects.filter(id=self.kwargs.get("id"))

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    lookup_field = "blog_id"

    def get_queryset(self):
        return Comment.objects.filter(blog=self.kwargs.get("blog_id"))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentView(UpdateAPIView, DestroyAPIView, CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Comment.objects.filter(id=self.kwargs.get("id"))

    def put(self, request, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        if not comment:
            return Response(
                {"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if comment.author != user and not user.role == "admin":
            return Response(
                {"error": "You are not allowed to update this comment"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        if not comment:
            return Response(
                {"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if comment.author != user and not user.role == "admin":
            return Response(
                {"error": "You are not allowed to update this comment"},
                status=status.HTTP_403_FORBIDDEN,
            )

        return self.destroy(request, *args, **kwargs)

    def post(self, request):
        request.data["author"] = request.user.id
        return self.create(request)
