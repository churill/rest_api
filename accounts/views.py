from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer


class CustomUserView(APIView):
    permission_classes = []

    def get(self, request):
        user = get_user_model().objects.all().order_by('user_id')
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.POST.get('user_id')
        try:
            user = get_user_model().objects.get(user_id=user_id)
        except get_user_model().DoesNotExist:
            return Response({'username': ''})
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


custom_user_view = CustomUserView.as_view()
