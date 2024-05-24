from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template
from django.contrib.auth import logout


# Create your views here.
def logedin(request:HttpRequest):
    template= get_template('dashboard.html')
    return HttpResponse(template.render({}, request))


def edit_profile(request:HttpRequest):
    template= get_template('edit_profile_page.html')
    return HttpResponse(template.render({}, request))


def logout_view(request):
    logout(request)
    return redirect('home')