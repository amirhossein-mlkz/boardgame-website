from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from django.contrib import messages
from notifications.signals import notify

from . models import Game, Team, Player, PredefineGame
from .forms import creatGameForm, CreatTeamForm, JoinGameForm



def games_archive(request:HttpRequest):
    template = get_template('games_archive.html')
    games = PredefineGame.objects.all()
    context = {'games':games}
    return HttpResponse(template.render(context, request))



def create_or_join_game(request:HttpRequest, game_slug:str):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    # for game in Game.objects.all():
    #     game.delete()
    try:
        game = Game.objects.get(creator_user = user, name = game_slug)
        return redirect('lobby', game_id = game.id)

    except Exception as e:
        pass
    
    try:
        player = Player.objects.get(user = user, game__name = game_slug)
        return redirect('lobby', game_id = player.game.id)
    except:
        pass

    template = get_template('create_or_join_game.html')

    if request.method == 'POST':
        
        #--------------------------CREAT GAME--------------------------
        if 'submit_create_game' in request.POST:
            create_game_from = creatGameForm(request.POST)
            if create_game_from.is_valid():
                password = create_game_from.cleaned_data['password1']
                
                game = Game(name = game_slug, password=password, creator_user=user)
                predefine_game = get_object_or_404(PredefineGame, slug=game_slug)

                game.is_team = predefine_game.is_team
                game.min_players = predefine_game.min_players
                game.max_players = predefine_game.max_players
                game.save()

                player = Player(user=user, game=game)
                player.save()
                return redirect('lobby',game.id)
        else:
            create_game_from = creatGameForm()


        #--------------------------JOIN GAME--------------------------
        if 'submit_join_game' in request.POST:
            join_game_form = JoinGameForm(request.POST)
            
            if join_game_form.is_valid():
                game_id = join_game_form.cleaned_data['game_id']
                game = Game.objects.get(id=game_id)
                player = Player(user=user, game=game)
                player.save()
                return redirect('lobby', game_id)
        else:
            join_game_form = JoinGameForm()

        

    else:
        create_game_from = creatGameForm()
        join_game_form = JoinGameForm()

    
    context = {
        'create_game_from': create_game_from,
        'join_game_form': join_game_form,

    }
    return HttpResponse(template.render(context=context, request=request))







def lobby(request:HttpRequest, game_id:str):
    # for game in Game.objects.all():
    #     game.delete()
    if not request.user.is_authenticated:
        redirect('login')
    

    game = get_object_or_404(Game, id=game_id)
    user = request.user
    game.creator_user == user
    try:
        player = Player.objects.get(user=request.user, game=game)
    except:
        if game.creator_user == user:
            game.delete()
        return redirect('games_archive')
    
    template = get_template('lobby.html')

    if request.method == 'POST':
        if 'submit_create_team' in request.POST:
            create_team_form = CreatTeamForm(request.POST)
            if create_team_form.is_valid():
                team = create_team_form.save(commit=False)
                team.game = game
                team.save()
                print('team',team)
        else:
            print('not valid')
            create_team_form = CreatTeamForm()

        
        if 'submit_remove_team' in request.POST:
            team_id = request.POST.get('team_id')
            try:
                team = Team.objects.get(id=team_id)
                team.delete()
            except:
                pass

        if 'submit_remove_player' in request.POST:
            player_id = request.POST.get('player_id')
            try:
                player = Player.objects.get(id=player_id)
                player.delete()
            except:
                pass
        
        if 'submit_join_team' in request.POST:
            team_id = request.POST.get('team_id')
            try:
                team = Team.objects.get(id=team_id)
                player.team = team
                player.save()

            except:
                pass


    else:
        create_team_form = CreatTeamForm()

    teams_data = []
    teams = Team.objects.filter(game=game)
    for team in teams:
        players = Player.objects.filter(team=team)
        teams_data.append({'team': team, 'players': players})
    
    all_players = Player.objects.filter(game=game)
    
    context = {
        'is_creator': game.creator_user == user,
        'create_team_form': create_team_form,
        'game': game,
        'teams_data': teams_data,
        'all_players':all_players,
    }

    return HttpResponse(template.render(context, request))








def remove_game(request:HttpRequest, game_id:str):
    if not request.user.is_authenticated:
        return redirect('login')
    

    game = get_object_or_404(Game, id=game_id)
    
    if game.creator_user == request.user:
        game_name = game.name
        game.delete()
        
        return redirect('games_archive')
    else:
        return redirect('home')
    

