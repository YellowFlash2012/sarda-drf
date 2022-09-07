

from django.urls import path
from watchlist_app.api.views import AddNewReview, GetAllMovies, GetAllReviews, GetAllStreamingPlatforms, GetOneReview, SingleMovie, SingleStreamingPlatform

urlpatterns = [
    # path('', get_all_movies, name='all-movies-list'),
    path('', GetAllMovies.as_view(), name='all-movies-list'),

    # path('<int:pk>', get_single_movie, name='single-movie'),
    path('<int:pk>', SingleMovie.as_view(), name='single-movie'),


    path('platform/', GetAllStreamingPlatforms.as_view(), name='all-streaming-platforms'),

    path('platform/<int:pk>', SingleStreamingPlatform.as_view(), name='single-streaming-platform'),

    path('<int:pk>/reviews/new', AddNewReview.as_view(), name='add-new-review'),
    
    path('<int:pk>/reviews', GetAllReviews.as_view(), name='all-reviews'),

    path('reviews/<int:pk>', GetOneReview.as_view(), name='single-review'),
]
