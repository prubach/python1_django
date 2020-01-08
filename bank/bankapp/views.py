from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Customer

def index(request):
    return HttpResponse('Hello in my Bank')

def hello(request):
    return HttpResponse('Hello')

def helloTemplate(request):
    msg = 'Hello in a template'
    return render(request, 'bankapp/test.html', {'hello_text': msg})

def show_customer(request, cust_id):
    customer = get_object_or_404(Customer, cust_id)
    return render(request, 'bankapp/cust.html', {'customer' : customer})
