from django.urls import path
from . import views

###local:8000/

urlpatterns = [
path('index', views.index),
path('Voice', views.Voice)

]