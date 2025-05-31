from django.urls import path
from user.views import ListUserView, update_user, get_top_three_members

urlpatterns = [
    path("list/", ListUserView.as_view(), name="user-list"),
    path("update/", update_user, name="user-update"),
    path("top-three/", get_top_three_members, name="get top three member"),
]
