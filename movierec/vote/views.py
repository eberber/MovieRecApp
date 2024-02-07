from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Movie

# Create your views here.
def index(request):
    #list of obj
    movie_list = Movie.objects.order_by("name")
    list = []
    nl = "\n"
    for m in movie_list:
        list.append(f"Movie Name: {m.name} {nl} Genre: {m.genre}")
    output = "\n ".join(list)
    return HttpResponse(output)