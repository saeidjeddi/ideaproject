from rest_framework.views import APIView
from rest_framework.response import Response

from apps.blog.models import ListPostModel
from apps.blog.serializers import ListPostSerializer, ListPostDetailSerializer, ListPostCreateSerializer, ListPostUpdateSerializer


class ListPostAPIView(APIView):
    serializer_class = ListPostSerializer
    def get(self, request):
        queryset = ListPostModel.objects.only(
            'id',
            'image',
            'title',
            'content',
            'author',
            'created_at',
            'updated_at',
        )
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ListPostDetailAPIView(APIView):
    serializer_class = ListPostDetailSerializer

    def get(self, request, pk):
        try:
            queryset = ListPostModel.objects.get(pk=pk)
            serializer = self.serializer_class(queryset)
            return Response(serializer.data)
        except ListPostModel.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)



class ListPostCreateAPIView(APIView):
    serializer_class = ListPostCreateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class ListPostUpdateAPIView(APIView):
    serializer_class = ListPostUpdateSerializer

    def put(self, request, pk):
        try:
            queryset = ListPostModel.objects.get(pk=pk)
            serializer = self.serializer_class(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)  # Ensure the author is set to the current user
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except ListPostModel.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
