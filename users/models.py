from django.db import models


class User(models.Model):
    username = models.CharField(blank=True, max_length=30)
    title = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='profile_images', blank=False)
    summary = models.TextField(default='', blank=False)

    def __str__(self):
        return self.username
