from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('user_login/', user_login, name='user_login'),
    path('otp/', otp, name='otp'),
    path('user_logout/', user_logout, name='user_logout'),
]
