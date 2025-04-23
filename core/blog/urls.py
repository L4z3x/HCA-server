from django.urls import path
from blog.views import (
    create_blog,
    like_blog,
    dislike_blog,
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
    path("<int:blog_id>/comments/", CommentListView.as_view(), name="get comments"),
    # comments:
    path("comment/<int:id>/", CommentView.as_view(), name="delete update comment"),
    path("comment/", CommentView.as_view(), name="create comment"),
    path("<int:blog_id>/like/", like_blog, name="like blog"),
    path("<int:blog_id>/dislike/", dislike_blog, name="dislike blog"),
]
