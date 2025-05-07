from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views.templat import robots_txt

urlpatterns = [
    path('panel-admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),

]



urlpatterns += [
    path('robots.txt', robots_txt, name='robots_txt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)