from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext=request.POST.get('text','default')

    #Check box
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST .get('newlineremover','off')

    #Check if checkbox is on
    if removepunc =="on":
         punctuations = ''' : ;"" ' ' ! -[]() {}'''
         analyzed =""
         for char in djtext:
             if char not in punctuations:
                analyzed=analyzed + char
         params={'purpose' :'Remove Punctuations','analyzed_text': analyzed}
         return render(request,'analyze.html',params)

    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Remove New Lines ', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

