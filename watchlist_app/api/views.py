
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from watchlist_app.models import Movie

# Create your views here.
@api_view(['GET', 'POST'])
def get_all_movies(request):
    if request.method == 'GET':
    # get query_sets
        movies = Movie.objects.all()

    # step2: serialize the query_set
        serializer = MovieSerializer(movies, many=True)

    # step3: return serializer
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def get_single_movie(request, pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response()