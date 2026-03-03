from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def index (request):
    # print(vars(request))
    return render(request, 'index.html')

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')

def dynamic_url(request, id, name):
    print(f"Dynamic URL: {id}")
    return render(request, 'dynamic_url.html', context={'id': id, 'name': name})

class HomeView(View):
    temlate_name = 'index.html'
    def get(self, request):
        return render(request, self.temlate_name)