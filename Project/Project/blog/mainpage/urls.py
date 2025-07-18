
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.index, name='mainpage'),
    path('menu/', views.menu),
    path('login/', auth_views.LoginView.as_view(
        template_name='user/login.html'),
        name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(next_page='/'),
         name='logout'),

    path('register/', views.register, name='register'),
    
]
