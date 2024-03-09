from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
     # ex: /vote/
    path("", views.index, name="index"),
     # ex: /vote/movie_id
     path("<int:movie_id>/", views.detail, name="detail"),
     path("like", views.like, name="like"),

]