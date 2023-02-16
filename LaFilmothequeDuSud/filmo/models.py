from django.db import models

class Director(models.Model):
    lastname = models.CharField(max_length=140, null=False)
    firstname = models.CharField(max_length=140, null=False)
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=255, null=True)

class Script(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=10000, null=False)
    #id_movie = models.OneToOneField(id, Movie, on_delete=models.CASCADE, null=True)

class Movie(models.Model):
    GENRE = [
        ("ACTION", "action"),
        ("SUSPENSE", "suspense"),
        ("HORROR", "horror"),
        ("ROMANTIC", "romantic"),
        ("COMEDY", "comedy"),
        ("UNDEFINED", "undefined"),
    ]
    id_director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False)
    id_script = models.ForeignKey(Script, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=10000)
    duration = models.IntegerField()
    genre = models.CharField(max_length=120, choices=GENRE)

class Actor(models.Model):
    firstname = models.CharField(max_length=140, null=False)
    lastname = models.CharField(max_length=140, null=False)
    age = models.IntegerField(null=True)

class Play(models.Model):
    id_movie = models.ManyToManyRel("id", Movie)
    id_actor = models.ManyToManyRel("id", Actor)
