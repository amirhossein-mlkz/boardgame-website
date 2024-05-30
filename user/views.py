from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, update_session_auth_hash
from django.template.loader import get_template
from django.contrib import messages

from .froms import UserLoginForm, EditUserForm, CustomPasswordChangeForm, UserRegisterForm
from .models import User

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




def register(request:HttpRequest):
    if request.user.is_authenticated:  # بررسی می‌کنیم که کاربر قبلاً لاگین کرده یا خیر
        return redirect('dashboard')
    
    template = get_template('register.html')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home') 
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return HttpResponse(template.render(context=context, request=request))
    






def logedin(request:HttpRequest):
    template= get_template('dashboard.html')
    return HttpResponse(template.render({}, request))


def edit_profile(request:HttpRequest):

    if not request.user.is_authenticated:  # بررسی می‌کنیم که کاربر قبلاً لاگین کرده یا خیر
        return redirect('home')
    
    #get loggedin user object
    username = request.user.get_username()

    user = get_object_or_404(User, phone_number=username)
    if request.method == 'POST':

        # name of submit button of this form in html
        if 'submit_edit_user' in request.POST:
            edit_user_form = EditUserForm(request.POST, instance=user, prefix='edit_user_form')
            if edit_user_form.is_valid():
                edit_user_form.save()
                messages.success(request, 'اطلاعات با موفقیت بروزرسانی شد')
            else:
                messages.error(request, 'اطلاعات وارد شده صحیح نمی‌باشد')
        else:
            edit_user_form = EditUserForm(instance=user, prefix='edit_user_form')


        # name of submit button of this form in html
        if 'submit_pass_change' in request.POST:
            pass_change_form = CustomPasswordChangeForm(request.user, request.POST, prefix='pass_change_form')
            
            if pass_change_form.is_valid():
                user = pass_change_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'رمز با موفقیت تغییر کرد')
            else:
                messages.error(request, 'تغییر رمز ناموق بود')
        else:
            pass_change_form = CustomPasswordChangeForm(user=user, prefix='pass_change_form')



    else:
        edit_user_form = EditUserForm(instance=user, prefix='edit_user_form')
        pass_change_form = CustomPasswordChangeForm(user=user, prefix='pass_change_form')


    context = {
        'edit_user_form': edit_user_form,
        'pass_change_form': pass_change_form,
    }
    template= get_template('edit_profile_page.html')
    return HttpResponse(template.render(context, request))


def logout_view(request:HttpRequest):
    auth_logout(request)
    return redirect('home')
