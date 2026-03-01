from django.http import HttpResponse

def index (request):
    return HttpResponse("Hello, Suman, Welcome to this Django Course")