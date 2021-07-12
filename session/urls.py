from django.urls import path
from .views import loginuser, logoutuser


urlpatterns = [
    path('login/',loginuser, name='login'),
    path('logout/',logoutuser, name='logout'),
]
