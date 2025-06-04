from django.shortcuts import render
from . import models

# Create your views here.

def posts(request):
    context = {
        'author': 'Я',
        'all_posts': models.Article.objects.all() 
        #Получить из БД все объекты Article
    }

    return render(
        request,
        'article/feed.html',

        context
    )

