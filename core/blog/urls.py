from django.urls import path
from blog.views import create_blog, BlogListView

urlpatterns = [
    path("create/", create_blog, name="create blog"),
    path("list/", BlogListView.as_view(), name="create blog"),
]
