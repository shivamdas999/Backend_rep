from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=256)
    isbn = models.CharField(max_length=20)
    authors = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    number_of_pages = models.IntegerField()
    country = models.CharField(max_length =100)
    released_date = models.DateField()
