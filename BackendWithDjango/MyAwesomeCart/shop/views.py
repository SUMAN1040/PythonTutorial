from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("about")

def contact(request):
    return HttpResponse("contact")

def tracker(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("search")

def productView(request):
    return HttpResponse("view")

def checkout(request):
    return HttpResponse("checkout")
