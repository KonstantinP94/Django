from django.shortcuts import render
from . import models
from datetime import datetime

# Create your views here.

def posts(request, **kwargs):
    print(request.GET)
    my_posts = models.Article.objects.filter(
        # dt__lt=datetime(2025,5,19) #фильтром выбраны посты позже до 19 мая
        user=kwargs['uid'] #request.GET.get('uid')
    )
    # __gt > greater than
    # __lt < less than
    # __gte >= greater than or equal
    # __lte <= less than or equal to
    context = {
        'author': 'Я',
        'uid': str(kwargs=['uid']),#request.GET.get('uid'),
        'all_posts': my_posts 
        #Получить из БД все объекты Article
    }

    return render(
        request,
        'article/feed.html',

        context
    )

from . import forms
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')

def publish(request):
    form = forms.BlogPostForm(request.POST)
    context = {
        'new_blog_post_form': form
    }
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    return render(
        request,
        'article/new.html',
        context
    )
