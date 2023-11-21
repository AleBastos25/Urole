from django.db import models
class Role(models.Model):
    name = models.CharField(max_length=255)
    dia = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name}'