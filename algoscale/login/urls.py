from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path(r'login', user_login),
    path(r'auth', auth_view),
    path(r'profile', profile),
    path(r'delete/user', delete_user),

]