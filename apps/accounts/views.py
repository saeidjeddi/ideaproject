from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class UseIfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'name': request.user.username,
            'phone': request.user.phone
        })