from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('', views.home, name='home'),


]