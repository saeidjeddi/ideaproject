from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView

from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
    



def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
