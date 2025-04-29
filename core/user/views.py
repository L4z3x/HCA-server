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

    def get_queryset(self):
        query = self.request.query_params
        if query.get("role") and query.get("departement"):
            return user.objects.filter(
                role=query.get("role"), departement=query.get("departement")
            )
        if query.get("role"):
            return user.objects.filter(role=query.get("role"))
        if query.get("departement"):
            return user.objects.filter(departement=query.get("departement"))

        return user.objects.all()

    def get(self, request):
        return self.list(request)
