from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    if removepunc == "on":
        #analyzed = djtext
         punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ""
         for char in djtext:
             if char not in punctuation:
                 analyzed += char
         params = {'purpose':'removepunc', 'analyzed_text': analyzed}
         djtext = analyzed

    if(fullcaps=='on'):
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed += char
        params = {'purpose': 'Remove newLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index + 1] == ' ':
                pass
            else:
                analyzed += char
        params = {'purpose': 'Extraspaced removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == 'on'):
        analyzed = 0
        for char in djtext:
            analyzed += 1

        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        djtext = analyzed


    if (removepunc != 'on' and fullcaps!='on' and newlineremover != 'on' and spaceremover != 'on' and charcount != 0):
         return HttpResponse('Please Select At least One Option.')

    return render(request, 'analyze.html', params)
