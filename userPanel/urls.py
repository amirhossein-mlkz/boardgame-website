from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.logedin, name='dashboard'),
    path('dashboard/edit-profile', views.edit_profile, name='edit-profile'),
    path('logout/', views.logout_view, name='logout'),

]
