from django.contrib import admin

from .models import PredefineGame
# Register your models here.
class PredefineGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_team', 'min_players', 'max_players')  # Remove 'creator_user'
    search_fields = ['name']

admin.site.register(PredefineGame, PredefineGameAdmin)