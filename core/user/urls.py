from django.urls import path
from user.views import ListUserView

urlpatterns = [
    path("list/", ListUserView.as_view(), name="user-list"),
]
