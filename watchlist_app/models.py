from django.db import models

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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

