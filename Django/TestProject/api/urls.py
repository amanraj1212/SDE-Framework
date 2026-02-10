from django.urls import path
from .views import my_func
urlpatterns = [
    path('a/', my_func, {'status':'OK'} ,name='my_func'),
]