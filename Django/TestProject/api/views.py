from django.shortcuts import render
from django.http import HttpResponse
from api.models import Profile, User
from .forms import Registration
from django.http import HttpResponseRedirect
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
