from django.contrib import admin

from .models import Movie, Director, Play, Script, Actor

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'genre', 'duration']

admin.site.register(Movie, MovieAdmin)

class ScriptAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']

admin.site.register(Script, ScriptAdmin)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'age']

admin.site.register(Director, DirectorAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'age']

admin.site.register(Actor, ActorAdmin)

class PlayAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_movie', 'id_actor']

admin.site.register(Play, PlayAdmin)