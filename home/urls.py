from django.urls import path
from .views.templat import HomeView


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'), # Home page
]