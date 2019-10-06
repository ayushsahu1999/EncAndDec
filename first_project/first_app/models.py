from django.db import models


# Create your models here.
class Crypt(models.Model):
    line = models.CharField(max_length = 264)

    def __str__(self):
        return self.line
