from django.urls import path
from .views import my_func, show, register, registration_success
urlpatterns = [
    path('a/', my_func, {'status':'OK'} ,name='my_func'),
    path('b/', show),
    path('c/', register),
    path('d/', registration_success)
]