from django.db import models

# Create your models here.

class Cook(models.Model):

    menu = (('salad', 'salad'),
             ('soup', 'soup'),
             ('dessert', 'dessert'))
    name = models.CharField(max_length=50)
    text = models.TextField()
    choice = models.CharField(max_length=20, choices=menu)
    price = models.IntegerField()
