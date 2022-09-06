

from django.urls import path
from watchlist_app.api.views import GetAllMovies, SingleMovie, get_all_movies, get_single_movie

urlpatterns = [
    # path('', get_all_movies, name='all-movies-list'),
    path('', GetAllMovies.as_view(), name='all-movies-list'),
    
    # path('<int:pk>', get_single_movie, name='single-movie'),
    path('<int:pk>', SingleMovie.as_view(), name='single-movie'),
]
