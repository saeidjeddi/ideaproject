from django.urls import path
from .views import UseIfo

urlpatterns = [
    path('', UseIfo.as_view(), name='user'),

]
