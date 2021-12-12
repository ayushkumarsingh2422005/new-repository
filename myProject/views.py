from django.http import HttpResponse
from django.shortcuts import render

import requests

#text = ''

def index(request):
    text = request.GET.get('aks')
    data_raw = requests.get('https://api2.sololearn.com/v2/codeplayground/usercodes/c5I5H9T7viyb')
    print(data_raw.json())
    return HttpResponse(text)


def index1(request):
    #prams = {'name':'ayush','class':'12'}
    return render(request, 'index.html')

def index2(request):
    #prams = {'name':'ayush','class':'12'}
    return HttpResponse('this is home page')
    
def page_not_found_view(request, exception):
    #prams = {'name':'ayush','class':'12'}
    return HttpResponse('error 404'+str(exception))
