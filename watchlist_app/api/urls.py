

from django.urls import path
from watchlist_app.api.views import get_all_movies, get_single_movie

urlpatterns = [
    path('', get_all_movies, name='all-movies-list'),
    path('<int:pk>', get_single_movie, name='single-movie'),
]
