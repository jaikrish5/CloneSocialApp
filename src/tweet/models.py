from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.urls import reverse

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    content = models.TextField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('tweet:detail',kwargs={'pk':self.pk})
