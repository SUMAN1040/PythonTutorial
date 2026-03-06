from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import random

def index (request):
    # print(vars(request))
    lucky_number = random.randint(100, 999)
    vegetables = ['Tomato', 'Cucumber', 'Carrot', 'Spinach']
    age = 22
    context = {"Lucky_number": lucky_number, "Vegetables": vegetables, "Age": age}
    return render(request, 'index.html', context)

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