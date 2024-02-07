from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Choice, Movie

# Create your views here.
def index(request):
    #list of obj
    movie_list = Movie.objects.order_by("name")
    type(movie_list)
    #movie_list = get_list_or_404(Movie.objects.order_by("name"))
    """    list = []
    nl = "\n"
    for m in movie_list:
        list.append(f"Movie Name: {m.name} {nl} Genre: {m.genre}")
    output = "\n ".join(list)"""
    context = {"movie_list": movie_list}
    return render(request, "vote/index.html", context)