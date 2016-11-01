from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=94)
    # author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    views = models.IntegerField(default=0)
    url = models.URLField(blank=True)

