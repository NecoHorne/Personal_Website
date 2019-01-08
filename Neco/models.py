from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=20, default='Title')
    tags = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="")
    github = models.URLField(null=True, blank=True)
    google_play = models.URLField(null=True, blank=True)
    web_url = models.URLField(null=True, blank=True)
    steam_url = models.URLField(null=True, blank=True)
    apple_store = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
