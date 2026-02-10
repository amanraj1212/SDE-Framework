from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_func(request, **kwargs):
    my_var = {'my_key': 12}
    return render(request, 'api/django.html', context=my_var)
