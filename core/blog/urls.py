from django.urls import path
from blog.views import create_blog, GetBlogView, BlogView, BlogListView

urlpatterns = [
    path("create/", create_blog, name="create blog"),
    path("list/", BlogListView.as_view(), name="create blog"),
    path("<int:id>/", GetBlogView.as_view(), name="get blog"),
    path("<int:id>/update/", BlogView.as_view(), name="update blog"),
    path("<int:id>/delete/", BlogView.as_view(), name="delete blog"),
    # path("")
]
