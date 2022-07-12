from django.db import models
from django.contrib.auth.models import User


class URLShortenerModel(models.Model):
    url = models.TextField(unique=True)
    new_url = models.CharField(unique=True, max_length=256)
    created_data = models.DateTimeField(auto_now_add=True)
    auth_user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.created_data}, {self.auth_user}'

    class Meta:
        verbose_name = 'Сокращенный путь'
        verbose_name_plural = 'Сокращенные пути'
