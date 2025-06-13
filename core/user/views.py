from user.models import user
from rest_framework.generics import ListAPIView
from user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.permissions import IsAdmin
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class ListUserView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

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


@permission_classes([IsAdmin])
@api_view(["POST"])
def update_user(request):
    """
    Update user score or departement or role. (batch or single)
    """
    ids = request.data.get("ids")
    score = request.data.get("score")
    departement = request.data.get("departement")
    role = request.data.get("role")
    if not score and not departement and not role:
        return Response({"error": "No data provided"}, status=400)
    if not ids:
        return Response({"error": "No ids provided"}, status=400)
    for id in ids:
        try:
            usr = user.objects.filter(id=id).first()
        except user.DoesNotExist:
            return Response({"error": f"User with id {id} does not exist"}, status=404)
        usr.score = score if score else usr.score
        usr.departement = departement if departement else usr.departement
        usr.role = role if role else usr.role
        usr.save()
    return Response({"success": "Users updated successfully"}, status=200)


@api_view(["GET"])
@permission_classes([AllowAny])
def get_top_three_members(request):
    """
    Get top three users with the highest scores.
    """
    top_users = user.objects.order_by("-score")[:3]
    serializer = UserSerializer(top_users, many=True)
    return Response(serializer.data, status=200)
