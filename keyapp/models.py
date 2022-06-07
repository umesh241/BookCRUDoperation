from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bookinfo'
