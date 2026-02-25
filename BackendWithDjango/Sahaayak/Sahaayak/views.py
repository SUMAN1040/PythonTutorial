from django.http import HttpResponse
# from django.http import JsonResponse
from django.shortcuts import render

def womenSafetyApplication(request):
    return HttpResponse("<h1>Hey Suman, Welcome you in this django learning path<h1/>")



def homeApplication(request):
    return HttpResponse("Hey Suman, Here we are just checking how whole django apps views are working")


def index(request):
    with open('Sahaayak/harry.txt', 'r') as note:
        return HttpResponse(note.read())
    

def web1(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <h2>Company Websites</h2>
    <ul>
        <li><a href="https://www.google.com" target="_blank">Google</a></li>
        <li><a href="https://www.facebook.com" target="_blank">Facebook</a></li>
        <li><a href="https://www.amazon.com" target="_blank">Amazon</a></li>
        <li><a href="https://www.microsoft.com" target="_blank">Microsoft</a></li>
        <li><a href="https://www.apple.com" target="_blank">Apple</a></li>
    </ul>
</body>

</html>""")


def home(request):
    nav = '''
            
            <h1>Home</h1>
    
             <li><a href="/removePunc/">Remove Punctuation</a></li>
             <li><a href="/capitalizeFirst/">Capitalization</a></li>
             <li><a href="/newLineRemove/">New Line Remover</a></li>
             <li><a href="/spaceRemove/">Space Remover</a></li>
             <li><a href="/charCount/">Charecter Counter</a></li>
            '''
    return HttpResponse(nav)


def removePunch(request):
    return HttpResponse("Remove Punch")

def capFirst(request):
    return HttpResponse("capitalize First")

def newLineRemove(request):
    return HttpResponse("New Line Remove")

def spaceRemove(request):
    return HttpResponse("space Remove")

def charCount(request):
    return HttpResponse("char Count")