from django.db import models
from user.models import User
# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=6)
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_team = models.BooleanField(default=False)
    min_players = models.IntegerField(default=0)
    max_players = models.IntegerField(default=10)




class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)



class Player(models.Model):
    game = models.ForeignKey(Game, on_delete= models.CASCADE)
    team = models.ForeignKey(Team, on_delete= models.CASCADE, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

