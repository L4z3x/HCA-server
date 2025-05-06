from django.urls import path
from user.views import ListUserView, update_user

urlpatterns = [
    path("list/", ListUserView.as_view(), name="user-list"),
    path("update/", update_user, name="user-update"),
]
