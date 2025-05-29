from django.urls import path
from .views.templat import HomeView
from .views.api import HomeView as api


app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'), # Home page
    path('api/', api.as_view(), name='index'), # Home page
]