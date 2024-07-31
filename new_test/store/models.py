from django.db import models

class Book(models.Model):
    tittle = models.CharField (max_length=250)
    slug =  models.SlugField (max_length=250)
    price = models.FloatField ()
