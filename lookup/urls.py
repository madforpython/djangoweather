
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('about.html',views.About,name='About'),
]
