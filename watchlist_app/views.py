from django.http import JsonResponse
from django.shortcuts import render

from watchlist_app.models import Movie

# Create your views here.
def get_all_movies(request):
    # get query_sets
    movies = Movie.objects.all()

    # step2: convert query_set into python dictionqry
    data={
        'movies': list(movies.values())
    }

    # step3: convert python dictionqry into json
    return JsonResponse(data)

def get_single_movie(request, pk):
    movie = Movie.objects.get(pk=pk)

    data = {
        "name":movie.name,
        "launched":movie.launched
    }

    return JsonResponse(data)