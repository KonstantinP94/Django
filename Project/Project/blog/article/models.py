

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Article(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
