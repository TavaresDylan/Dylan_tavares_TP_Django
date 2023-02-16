from rest_framework.viewsets import ModelViewSet
from .serializers import DirectorSerializer, ActorSerializer, MovieSerializer, ScriptSerializer, PlaySerializer
from .models import Director, Actor, Movie, Script, Play

class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    
    def get_queryset(self):
        queryset =  Director.objects.all()

        country_param = self.request.GET.get("country")

        if country_param is not None:
            queryset = queryset.filter(country=country_param)

        return queryset

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

    
class PlayViewSet(ModelViewSet):
    serializer_class = PlaySerializer

    def get_queryset(self):
        return Play.objects.all()
