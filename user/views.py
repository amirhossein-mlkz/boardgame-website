from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.template.loader import get_template
from django.contrib import messages

from .froms import UserLoginForm

def login(request:HttpRequest):

    if request.user.is_authenticated:  # بررسی می‌کنیم که کاربر قبلاً لاگین کرده یا خیر
        return redirect('dashboard')
        
    
    template = get_template('login.html')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور صحیح نیست')
        else:
            messages.error(request, ' اطلاعات صحیح نیست')
    else:
        form = UserLoginForm()

    context = {
        "form": form
    }
    return HttpResponse(template.render(context=context, request=request))




