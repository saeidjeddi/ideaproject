from django.urls import path, re_path
from apps.blog.views.api import ListPostAPIView, ListPostDetailAPIView, ListPostCreateAPIView, ListPostUpdateAPIView, ListPostDeleteAPIView



app_name = 'blog'


urlpatterns = [
    path('', ListPostAPIView.as_view(), name='list'),
    path('<int:pk>/', ListPostDetailAPIView.as_view(), name='detail'),
    path('create/', ListPostCreateAPIView.as_view(), name='create'),
    path('update/<int:pk>/', ListPostUpdateAPIView.as_view(), name='update'),
    path('blog/delete/<int:pk>/', ListPostDeleteAPIView.as_view(), name='delete_post'),



]