from django.shortcuts import render
from Movieapp.models import Actor,Director,Movie
# Create your views here.
def home(request):
    all_movie_info = Movie.objects.all()
    return render(request,'Home/home.html',{'movies':all_movie_info})

def oneMovie(request,key):
    one_movie = Movie.objects.get(pk=key)
    date = str(one_movie.r_date)
    return render(request,'Movie/oneMovie.html',{'one_movie':one_movie,'date':date})

def oneActor(request,key):
    one_actor = Actor.objects.get(pk=key)
    date = str(one_actor.b_date)
    return render(request,'Actor/actor.html',{'one_actor':one_actor,'date':date})

def oneDirector(request,key):
    one_director = Director.objects.get(pk=key)
    date = str(one_director.b_date)
    return render(request,'Director/director.html',{'one_director':one_director,'date':date})