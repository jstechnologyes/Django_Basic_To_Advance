from django.urls import path
from .views import loginuser, logoutuser,registration
app_name='session'

urlpatterns = [
    path('login/',loginuser, name='login'),
    path('logout/',logoutuser, name='logout'),
    path('signup/',registration, name='signup'),
]
