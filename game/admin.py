from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PlayerUser, Game, Board,Question

admin.site.register(PlayerUser)
admin.site.register(Game)
admin.site.register(Board)
admin.site.register(Question)