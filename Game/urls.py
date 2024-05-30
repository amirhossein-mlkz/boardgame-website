from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_archive , name='games_archive'),
    path('create/<slug:game_slug>', views.create_or_join_game , name='create_or_join_game'),
    path('lobby/<slug:game_id>', views.lobby, name='lobby'),
    path('remove/<slug:game_id>', views.remove_game, name='remove_game'),

]
