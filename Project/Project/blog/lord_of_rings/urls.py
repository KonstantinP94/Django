from django.urls import path
from . import views

urlpatterns = [
    path('', views.lord_of_rings, name='lord_of_rings'),
]
