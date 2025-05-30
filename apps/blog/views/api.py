from rest_framework.views import APIView
from rest_framework.response import Response

from apps.blog.models import ListPostModel
from apps.blog.serializers import ListPostSerializer


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




