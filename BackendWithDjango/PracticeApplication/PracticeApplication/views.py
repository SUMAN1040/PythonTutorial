from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import random

def index (request):
    # print(vars(request))
    lucky_number = random.randint(100, 999)
    vegetables = ['Tomato', 'Cucumber', 'Carrot', 'Spinach']
    age = 22
    cities = [
        {'name': 'New York', 'population': 8000000, "country": "USA"},
        {'name': 'Los Angeles', 'population': 4000000, "country": "USA"},
        {'name': 'Chicago', 'population': 2700000, "country": "USA"},
        {'name': 'Houston', 'population': 2300000, "country": "USA"},
        {'name': 'Phoenix', 'population': 1600000, "country": "USA"},
    ]
    context = {"cities": cities, "Lucky_number": lucky_number, "Vegetables": vegetables, "Age": age}
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
        



# Project Creating 
def project(request):
    lucky_number = random.randint(100, 999)
    context = {"Lucky_number": lucky_number}
    
    return render(request, "project/project.html")