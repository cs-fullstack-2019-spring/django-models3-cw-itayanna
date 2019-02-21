
#importing models function

from django.db import models


# Create your models here.


#  name, pageNumber, genre, and publishDate attributes

class Book(models.Model):
    name = models.CharField(default="", max_length=1000)
    pageNumber = models.IntegerField()
    publishDate = models.DateField(default='')