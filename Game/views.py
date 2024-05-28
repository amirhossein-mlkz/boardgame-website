from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template

from . models import Game
from .forms import creatGameForm



def creat_game(request:HttpRequest, game_name:str):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user

    try:
        game = Game.objects.get(creator_user = user, name = game_name)
        return redirect('game_room')

    except Exception as e:
        
        template = get_template('create_game.html')

        if request.method == 'POST':
            form = creatGameForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password1']
                game = Game(name = game_name, password=password, creator_user=user)
                game.save()
                return redirect('game_room')
        else:
            form = creatGameForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context=context, request=request))


def game_room(req):
    # for game in Game.objects.all():
    #     game.delete()
    return HttpResponse('شما قبل بازی را ساخته اید')

