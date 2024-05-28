from django.urls import path
from . import views

urlpatterns = [
    
    path('create/<slug:game_name>', views.creat_game , name='create_grame'),
    path('game_room', views.game_room, name='game_room')
]
