from django.db import models
from accounts.models import Profile


# Create your models here.
class Topics(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_written = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)


class Comments(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_written = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=400)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
