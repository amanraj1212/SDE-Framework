from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, User
from .forms import Registration
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.

def my_func(request, **kwargs):
    my_var = {'my_key': 12}
    return render(request, 'api/django.html', context=my_var)
def show(req):
    stu = Profile.objects.all()
    print(stu)
    v = Profile.objects.get(name='Aryaman')
    print(v.surname)
    return HttpResponse()

def register(request):
    if request.method=='POST':
        f = Registration(request.POST)
        if f.is_valid():
            #print(f.cleaned_data)
            nm = f.cleaned_data['name']
            em = f.cleaned_data['email']
            u = User(name=nm,email=em)
            u.save()
            return HttpResponseRedirect('/d')
    else:
        f = Registration()
    return render(request,'api/django.html',{'form':f})

def registration_success(request):
    return render(request, 'api/success.html')

# server se client mai set kar rhe
def setcookie(request):
    response = render(request, 'api/setcookie.html')
    response.set_cookie('cookie_iss_naam_se_jana_jayega', 'cookie_key_val_123', max_age=5)
    return response

# client se server mai kaise get karenge
def getcookie(request):
    response = render(request, 'api/getcookie.html')
    #get_cookie_from_client = request.COOKIES['cookie_iss_naam_se_jana_jayega']
    # when you want to see some deault value when cookie is delete then:
    get_cookie_from_client = request.COOKIES.get('cookie_iss_naam_se_jana_jayega','default123')
    print(get_cookie_from_client)
    return response

def delcookie(request):
    response = render(request, 'api/delcookie.html')
    response.delete_cookie('cookie_iss_naam_se_jana_jayega')
    return response

class MyClassView1(View):
    def get(self,request):
        return HttpResponse("Hellow from class based View")

def another_my_func(request):
    p = serialize('json',Profile.objects.all())
    return JsonResponse(p,safe=False)
