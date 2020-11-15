from django.http import HttpResponse
from django.shortcuts import render

def analyse(request):
    djtext = request.POST.get('text', 'default')
  #checks are checked
    djtex_chk=request.POST.get('analyse_text', 'default')
    upperText_chk = request.POST.get('upper_text', 'default')
    new_line_remover=request.POST.get('new_line_remover', 'default')
    space_remover = request.POST.get('space_remover', 'default')

    if (djtex_chk=="on"):
        puncutuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in puncutuations:
                analyzed=analyzed+ char
        params={'purpose':'Removed Poncuations','analyzed_text':analyzed}
        djtext=analyzed

    if(upperText_chk=="on"):
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
    if(space_remover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
              analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
    if (new_line_remover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
    if (new_line_remover != "on" and space_remover !="on" and upperText_chk!="on" and  djtex_chk !="on"):
       return HttpResponse("ERROR")
    return render(request, 'analyzetext.html', params)

def index1(request):
    return render(request,'index1.html')