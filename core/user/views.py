from user.models import user
from rest_framework.generics import ListAPIView
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class ListUserView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # TODO: Change to admin

    """
    List all users.
    """

    model = user
    template_name = "user/list.html"
    context_object_name = "users"

    def get_queryset(self):
        return user.objects.all()

    def get(self, request):
        return self.list(request)
