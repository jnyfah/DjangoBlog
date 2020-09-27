from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

class PublishedManager(models.Model):
    def get_queryset(self):
        return super(PublishedManager, self) .get_queryset().filter(status='publish')

class Post(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    published = models.DateField(default=timezone)

    class meta:
        ordering = ('-published')
        
    def __str__(self):
        return self.title
