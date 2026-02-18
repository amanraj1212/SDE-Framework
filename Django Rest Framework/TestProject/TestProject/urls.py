from django.contrib import admin
from django.urls import path
from api.views import student_detail, student_create, student_update
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', student_detail),            # GET all
    path('b/', student_create),            # POST
    path('c/<int:pk>/', student_update),   # PUT / PATCH / DELETE
    path('d/', obtain_auth_token),
]
