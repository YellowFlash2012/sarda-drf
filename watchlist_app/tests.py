from rest_framework.authtoken.models import Token

from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser

from watchlist_app.models import Movie, Review, StreamingPlatform

# Create your tests here.
class StreamPlatformTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email="test@test.io", password="testpassword")

        self.token = Token.objects.get(user__email = self.user)

        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

        self.streamPlatform = StreamingPlatform.objects.create(name="prime+",
            about="Ultra 4K video",
            website="https://prime-plus.io")

    def test_streamplatform_create(self):

        data ={
            "name":"prime+",
            "about":"Ultra 4K video",
            "website":"https://prime-plus.io",
        }

        res = self.client.post(reverse('all-streaming-platforms'), data)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        res = self.client.get(reverse('all-streaming-platforms'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_single_streamplatform(self):
        res = self.client.get(reverse('single-streaming-platform', args = (self.streamPlatform.id)))

class MovieTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="test@test.io", password="testpassword")

        self.token = Token.objects.get(user__email = self.user)

        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

        self.streamPlatform = StreamingPlatform.objects.create(name="prime+",
            about="Ultra 4K video",
            website="https://prime-plus.io")

        self.movie = Movie.objects.create(platform = self.streamPlatform, title="blablabla", description="blablabla",launched=True)

    def test_movie_create(self):
        data = {
            "platform":self.streamPlatform,
            "title":"blablabla",
            "description":"blablabla",
            "launched":True,
        }

        res = self.client.post(reverse('all-movies-list'), data)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_movie_list(self):
        res = self.client.get(reverse('all-movies-list'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_single_movie(self):
        res = self.client.get(reverse('single-movie', args=(self.movie.id)))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(email="test@test.io", password="testpassword")

        self.token = Token.objects.get(user__email = self.user)

        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

        self.streamPlatform = StreamingPlatform.objects.create(name="prime+",
            about="Ultra 4K video",
            website="https://prime-plus.io")

        self.movie = Movie.objects.create(platform = self.streamPlatform, title="blablabla", description="blablabla",launched=True)

        self.review = Review.objects.create(author=self.user, movie=self.movie, review_text="blablabla", rating=4, published=False)

    def test_review_create(self):
        data = {
            "author":self.user,
            "movie":self.movie,
            "review_text":"blablabla",
            "rating":7,
            "published":True,
        }

        res = self.client.post(reverse('add-new-review', args=(self.movie.id,)), data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_review_update(self):
        data = {
            "author":self.user,
            "movie":self.movie,
            "review_text":"After watching the trailer",
            "rating":4,
            "published":False,
        }

        res = self.client.put(reverse('single-review', args=(self.review.id,)), data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_review_list(self):
        res = self.client.get(reverse('all-reviews', args=(self.movie.id,)))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_single_review(self):
        res = self.client.get(reverse('single-review', args=(self.review.id,)))

        self.assertEqual(res.status_code, status.HTTP_200_OK)