# Generated by Django 4.2.11 on 2024-05-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_players',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='min_players',
            field=models.IntegerField(default=0),
        ),
    ]
