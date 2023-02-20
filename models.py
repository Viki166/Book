from django.db import models
from django.db.models import ForeignKey,OneToOneField
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
