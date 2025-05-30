from django.urls import path, re_path
from apps.blog.views.api import ListPostAPIView



app_name = 'blog'


urlpatterns = [
    path('', ListPostAPIView.as_view(), name='list'),
]