from django.db import models
from django.contrib.auth.models import User


class URLShortenerModel(models.Model):
    url = models.TextField()
    new_url = models.CharField(max_length=256)
    created_data = models.DateTimeField(auto_now_add=True)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT)
