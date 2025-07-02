from django.shortcuts import render
from requests import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class UseIfo(APIView):
    permission_classes = [IsAuthenticated ]

    def get(self, request):
        return Response({
            'name': 'request.user.username'
        })

