
from django.forms import ValidationError
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewAuthorOrReadOnly
from watchlist_app.api.serializers import MovieSerializer, ReviewSerializer, StreamingPlatformSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from watchlist_app.models import Movie, Review, StreamingPlatform

# Create your views here.

# ***class based views
class GetAllMovies(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SingleMovie(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error":"Such movie doesn't exist!"}, status = status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

class GetAllStreamingPlatforms(APIView):
    def get(self, request):
        platforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(platforms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SingleStreamingPlatform(APIView):
    def get(self, request, pk):
        try:
            platform = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({"Error":"Such movie doesn't exist!"}, status = status.HTTP_404_NOT_FOUND)

        serializer = StreamingPlatformSerializer(platform)

        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        platform.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)

# class get_all_reviews(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class single_review(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
class AddNewReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk = pk)

        review_author = self.request.user
        review_queryset = Review.objects.filter(movie=movie, author=review_author)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        serializer.save(movie=movie, author=review_author)
class GetAllReviews(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(movie=pk)

class GetOneReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewAuthorOrReadOnly]

    # def get_queryset(self):
    #     pk = self.kwargs['pk']
    #     return Review.objects.filter(movie=pk)

# ***functional views
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
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({"Error":"Such movie doesn't exist!"}, status = status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)