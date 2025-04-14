from django.urls import path
from blog.views import (
    create_blog,
    GetBlogView,
    BlogView,
    BlogListView,
    CommentListView,
    CommentView,
)

urlpatterns = [
    path("create/", create_blog, name="create blog"),
    path("list/", BlogListView.as_view(), name="create blog"),
    path("details/<int:id>/", GetBlogView.as_view(), name="get blog"),
    path("<int:id>/", BlogView.as_view(), name="update blog"),
    path("comments/<int:blog_id>/", CommentListView.as_view(), name="get comments"),
    # comments:
    path("comment/<int:id>/", CommentView.as_view(), name="delete update comment"),
    path("comment/", CommentView.as_view(), name="create comment"),
]
