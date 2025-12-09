from . import views

from django.urls import path


app_name='account'
urlpatterns=[
    path("login/",views.user_login, name='login'),
    path("logout/",views.user_logout, name='logout'),
    path("",views.dashboard, name='dashboard'),
]