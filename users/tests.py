from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import CustomUser

# Create your tests here.
class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "username":"testcase",
            "email":"testcase@exe.io",
            "password":"testpassword",
            "password2":"testpassword"
        }

        res = self.client.post(reverse('users-signup'), data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user=CustomUser.objects.create_user(email="testcase@exe.io", password="testpassword")

    def test_login(self):
        data = {
            "email":"testcase@exe.io",
            "password":"testpassword"
        }

        res = self.client.post(reverse('users-login'), data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__email="testcase@exe.io")
        
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)

        res = self.client.post(reverse('users-logout'))

        self.assertEqual(res.status_code, status.HTTP_200_OK)