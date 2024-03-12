from django.shortcuts import render, get_list_or_404
from django.http import Http404, HttpResponse
from .models import User, Movie
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    #list of obj
   # movie_list = Movie.objects.order_by("name")
    #type(movie_list)
    movie_list = get_list_or_404(Movie.objects.order_by("name"))
    #controls items per page
    paginator = Paginator(movie_list, 9)
    """    list = []
    nl = "\n"
    for m in movie_list:
        list.append(f"Movie Name: {m.name} {nl} Genre: {m.genre}")
    output = "\n ".join(list)"""
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    #context = {"movie_list": movie_list}
    context = {"page_obj": page_obj}
    return render(request, "vote/index.html", context)

def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except movie.DoesNotExist:
        raise Http404("Movie does not exist")
    return render(request, "vote/detail.html", {"movie": movie})

def like(request, movie_id):
    temp_user = "Tom"
    if not User.objects.filter(name=temp_user).exists():
        print("CREATING NEW USER")
        user = User.objects.create(name = temp_user)
    user = User.objects.get(name=temp_user)
    #print(user.movie.all())
    movie_obj = Movie.objects.filter(id=movie_id)
    if movie_obj not in user.movie.all():
        print("ADDING NEW MOVIE OBJ")
        user.movie.add(movie_id)
    print(user.movie.all())
    movie_name = movie_obj[0].name
    context = {"user":user, "movie_name": movie_name}
    return render(request, "vote/like.html", context)