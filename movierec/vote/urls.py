from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
     # ex: /vote/
    path("", views.index, name="index"),
     # ex: /vote/movie_id
     path("<int:movie_id>/", views.detail, name="detail"),
     path("like/<int:movie_id>/", views.like, name="like"),
     path("recommender/", views.movie_recomender, name="recommender"),

]