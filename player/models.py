from django.db import models


class Team(models.Model):
    name = models.CharField(blank=False, null=False, max_length=250)




# Create your models here.
class Player(models.Model):
    name = models.CharField(blank=False, null=False, max_length=250)
    password = models.CharField(blank=False, max_length=250)


