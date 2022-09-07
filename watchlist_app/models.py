from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from watchmeproject.settings import AUTH_USER_MODEL


# Create your models here.

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name="movie")

    launched = models.BooleanField(default=True)

    avg_rating = models.FloatField(default=0)
    num_rating = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)])

    review_text = models.TextField(null=True)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")

    published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.movie.title