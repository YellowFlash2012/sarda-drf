from django.contrib import admin
from watchlist_app.models import Movie, Review, StreamingPlatform

# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamingPlatform)
admin.site.register(Review)