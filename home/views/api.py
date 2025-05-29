from rest_framework.response import Response
from rest_framework.views import APIView




class HomeView(APIView):
    def get(self, request):
        return Response({'hejjjjjjjllo': 'world111115555555555555555555555555555555511111111'})
