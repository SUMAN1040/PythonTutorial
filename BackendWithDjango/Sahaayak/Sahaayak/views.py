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
    
            # <li><a href="/removePunc/">Remove Punctuation</a></li>
            <li><a href="/capitalizeFirst/">Capitalization</a></li>
            <li><a href="/newLineRemove/">New Line Remover</a></li>
            <li><a href="/spaceRemove/">Space Remover</a></li>
            <li><a href="/charCount/">Character Counter</a></li>
            '''
    return HttpResponse(nav)


def analyze(request):
    #Get the text
    djText = request.POST.get('Info', 'default')
    
    #Check checkbox values
    removepunc = request.POST.get('remove', 'off')
    fullCap = request.POST.get('fullCaps', 'off')
    lineRemover = request.POST.get('lineRemover', 'off')
    extraSpaceRemover = request.POST.get('spaceRemover', 'off')
    charCounts = request.POST.get('charCount', 'off')
    # print(removepunc)
    # print(djText)
    #Analyze the text
    # return HttpResponse("Remove Punch")

# check which checkbox is on
#Punctuation to remove
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djText:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)
#Full Capitalization
    if (fullCap == "on"):
        analyzed = ""
        for char in djText:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'Full Capitalization', 'analyzed_text': analyzed}
            djText = analyzed
        # return render(request, 'analyze.html', params)
#New Line Remover
    if lineRemover == "on":
        analyzed = ""
        for char in djText:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {
        'purpose': 'Remove Extra New Lines',
        'analyzed_text': analyzed
        }
        djText = analyzed
        # return render(request, 'analyze.html', params)
#Extra Space Remover
    if (extraSpaceRemover == 'on'):
        analyzed = ""
        for index, char in enumerate(djText):
            if djText[index] == " " and djText[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djText = analyzed
        # return render(request, 'analyze.html', params)
#Character Count
    if (charCounts == 'on'):
        count = 0
        for char in djText:
            if char != " ":
                count += 1
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed, 'char_count': count}
    
    if(removepunc != "on" and fullCap != "on" and lineRemover != "on" and extraSpaceRemover != "on" and charCounts != "on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request, 'analyze.html', params)

def capFirst(request):
    return HttpResponse("capitalize First")

def newLineRemove(request):
    return HttpResponse("New Line Remove")

def spaceRemove(request):
    return HttpResponse("space Remove")

def charCount(request):
    return HttpResponse("char Count")


def template(request):
    # params = {'name' : 'Suman', 'Place' : 'Jaipur'}
    return render(request, 'index.html')
