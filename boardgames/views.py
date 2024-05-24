


from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home(request:HttpRequest):
    template = get_template('home.html')
    return HttpResponse(template.render(context={}, request=request))