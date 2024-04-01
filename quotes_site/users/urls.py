from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path('signup/', views.singupuser, name='signup'),         #users:signup
    path('login/', views.loginuser, name='login'),            #users:login
    path('logout/', views.logoutuser, name='logout'),         #users:logout
]