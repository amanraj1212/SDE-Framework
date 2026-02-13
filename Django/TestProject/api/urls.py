from django.urls import path
from .views import (my_func, show, register, registration_success, 
setcookie, getcookie,delcookie, MyClassView1, another_my_func)
urlpatterns = [
    path('a/', my_func, {'status':'OK'} ,name='my_func'),
    path('b/', show),
    path('c/', register),
    path('d/', registration_success),
    path('set/', setcookie),
    path('get',getcookie),
    path('del',delcookie),
    path('e/',MyClassView1.as_view(),name="myclassview1"),
    path('f',another_my_func),
]