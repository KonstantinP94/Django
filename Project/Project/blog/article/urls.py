from django.urls import path
from . import views

urlpatterns = [
    path('<int:uid>/', views.posts, name='blogpost'),
    path('new/', views.publish, name='save_articles'),
]