from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=94)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    views = models.IntegerField(default=0)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title