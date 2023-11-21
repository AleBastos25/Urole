from django.db import models
from django.conf import settings
class Role(models.Model):
    name = models.CharField(max_length=255)
    dia = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    dia = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username} ({self.dia})'