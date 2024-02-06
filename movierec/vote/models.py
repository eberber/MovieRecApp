from django.db import models
#must be an iterable containing (actual value, human readable name) tuples.
LANGUAGE_CHOICES = (
    ("Dutch", "DUTCH"),
    ("English", "ENGLISH"),
    ("German", "GERMAN"),
    ("Japanese", "JAPANESE"),
    ("Spanish", "SPANISH"),    
)
GENRE_CHOICES = (
    ('action', 'ACTION') ,
('adventure', 'ADVENTURE') ,
('animation', 'ANIMATION') ,
('biography', 'BIOGRAPHY') ,
('comedy', 'COMEDY') ,
('crime', 'CRIME') ,
('cult movie', 'CULT MOVIE') ,
('disney', 'DISNEY') ,
('documentary', 'DOCUMENTARY') ,
('drama', 'DRAMA') ,
('erotic', 'EROTIC') ,
('family', 'FAMILY') ,
('fantasy', 'FANTASY') ,
('film-noir', 'FILM-NOIR') ,
('gangster', 'GANGSTER') ,
('gay and lesbian', 'GAY AND LESBIAN') ,
('history', 'HISTORY') ,
('horror', 'HORROR') ,
('military', 'MILITARY') ,
('music', 'MUSIC') ,
('musical', 'MUSICAL') ,
('mystery', 'MYSTERY') ,
('nature', 'NATURE') ,
('neo-noir', 'NEO-NOIR') ,
('period', 'PERIOD') ,
('pixar', 'PIXAR') ,
('road movie', 'ROAD MOVIE') ,
('romance', 'ROMANCE') ,
('sci-fi', 'SCI-FI') ,
('short', 'SHORT') ,
('spy', 'SPY') ,
('super hero', 'SUPER HERO') ,
('thriller', 'THRILLER') ,
('visually stunning', 'VISUALLY STUNNING') ,
('war', 'WAR') ,
('western', 'WESTERN') ,
)

AGE_RATING_LIST=(
    ('G', 'G') ,
('PG', 'PG') ,
('PG-13', 'PG-13') ,
('R', 'R') ,
('NC-17', 'NC-17') 
)
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=100, blank=True)
    actors = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=1000, blank=True)
    age_rating = models.CharField(max_length=10,choices = AGE_RATING_LIST, default='G') #family friendly
    genre = models.CharField(max_length=50, choices = GENRE_CHOICES, default= '') #create movies, check genre here against list
    length = models.CharField(max_length=20, blank=True)
    languages = models.CharField(max_length=50, choices = LANGUAGE_CHOICES, default= 'English')
    

class Choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    liked = models.BooleanField(default = False)



    