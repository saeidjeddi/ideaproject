from django.urls import path, re_path
from apps.blog.views.api import ListPostAPIView, ListPostDetailAPIView



app_name = 'blog'


urlpatterns = [
    path('', ListPostAPIView.as_view(), name='list'),
    path('<int:pk>/', ListPostDetailAPIView.as_view(), name='detail'),
]