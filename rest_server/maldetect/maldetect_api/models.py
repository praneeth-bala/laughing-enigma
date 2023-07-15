from django.db import models
from django.contrib.auth.models import User

class XML(models.Model):
    xml = models.CharField(max_length=1000000)

    def __str__(self):
        return self.xml