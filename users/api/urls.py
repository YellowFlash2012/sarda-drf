from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api.views import logout_view, signup_view

urlpatterns=[
    path('login/', obtain_auth_token, name='users-login'),
    path('', signup_view, name='users-signup'),
    path('logout/', logout_view, name='users-logout'),
]