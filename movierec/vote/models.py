from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)
    age_rating = models.IntegerField(default=13) #family friendly
    genre = models.CharField(max_length=50) #create movies, check genre here against list
    languages = models.CharField(max_length=50)
    

class Choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    liked = models.BooleanField(default = False)



    