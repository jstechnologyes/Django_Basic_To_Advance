from django.urls import path
from .views import loginuser, logoutuser,registration,change_password
app_name='session'

urlpatterns = [
    path('login/',loginuser, name='login'),
    path('logout/',logoutuser, name='logout'),
    path('signup/',registration, name='signup'),
    path('password/',change_password, name='password'),
]
