from django.urls import path, include
from portfolio import views
from . import views


urlpatterns = [
    path('', views.home, name='home'),    
]

