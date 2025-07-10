from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(
        request,
        'mainpage/main.html'
    )

def menu(request):
    return render(
        request,
        'mainpage/menu.html'
    )

from . import forms
from django.contrib import auth

def register(request):
    user_form = forms.UserRegistrationForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=False)   # Создать, но в базу не записывать!
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()  
            auth.login(request, new_user)
            return redirect('/')
    return render(
        request,
        'user/register.html', {
            'form': user_form        })