from rest_framework.viewsets import ModelViewSet
from .serializers import DirectorSerializer, ActorSerializer, MovieSerializer, ScriptSerializer
from .models import Director, Actor, Movie, Script

class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    
    def get_queryset(self):
        return Director.objects.all()

class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer

    def get_queryset(self):
        return Actor.objects.all()
    
class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.all()

class ScriptViewSet(ModelViewSet):
    serializer_class = ScriptSerializer

    def get_queryset(self):
        return Script.objects.all()
