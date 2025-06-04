

# Register your models here.
from django.contrib import admin

from . import models

# models.НашКласс
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['dt', 'title', 'user']