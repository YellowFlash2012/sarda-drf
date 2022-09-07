from django.contrib import admin
from watchlist_app.models import Movie, StreamingPlatform

# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamingPlatform)