from django.urls import path
from blog.views import create_blog, get_blogs_list

urlpatterns = [
    path("create/", create_blog, name="create blog"),
    path("list/", get_blogs_list, name="create blog"),
]
