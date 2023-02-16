from rest_framework.serializers import ModelSerializer
from .models import Director, Actor, Movie, Script, Play

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'firstname', 'lastname', 'age', 'country']

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'

class PlaySerializer(ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'