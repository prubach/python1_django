from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello in my Bank')

def hello(request):
    return HttpResponse('Hello')

def helloTemplate(request):
    msg = 'Hello in a template'
    return render(request, 'bankapp/test.html', {'hello_text': msg})