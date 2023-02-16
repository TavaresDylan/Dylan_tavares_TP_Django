from django.db import models

class Director(models.Model):
    lastname = models.CharField(max_length=140, null=False)
    firstname = models.CharField(max_length=140, null=False)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.lastname

class Script(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=10000, null=False)
    #id_movie = models.OneToOneField(id, Movie, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    GENRE = [
        ("ACTION", "action"),
        ("SUSPENSE", "suspense"),
        ("HORROR", "horror"),
        ("ROMANTIC", "romantic"),
        ("COMEDY", "comedy"),
        ("UNDEFINED", "undefined"),
    ]
    id_director = models.ForeignKey(Director, related_name="director", on_delete=models.CASCADE, null=False)
    id_script = models.ForeignKey(Script, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=10000)
    duration = models.IntegerField()
    genre = models.CharField(max_length=120, choices=GENRE)

    def __str__(self):
        return self.title

class Actor(models.Model):
    firstname = models.CharField(max_length=140, null=False)
    lastname = models.CharField(max_length=140, null=False)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.lastname

class Play(models.Model):
    id_movies = models.ManyToManyField(Movie)
    id_actor = models.ManyToManyField(Actor)
