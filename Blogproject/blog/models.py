from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    published = models.DateField(default=timezone.now())

    class meta:
        ordering = ('-published')
        
    def __str__(self):
        return self.title