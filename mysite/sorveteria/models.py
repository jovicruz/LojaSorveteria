from django.db import models

# Create your models here.

class Items(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.FloatField()
    item_stock = models.IntegerField()

    def __str__(self):
        return self.item_name
        