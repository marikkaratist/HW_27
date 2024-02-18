from django.db import models


class Ad(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(max_length=100)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
