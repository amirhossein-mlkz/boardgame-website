from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse, HttpRequest

# Create your views here.

def user_login(request:HttpRequest):
    template = get_template('login.html')
    
    return HttpResponse(template.render({}, request))
