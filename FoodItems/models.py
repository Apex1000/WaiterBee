from django.db import models

# Create your models here.
class Item(models.Model):
    itemname = models.CharField(max_length=255)
    prise = models.IntegerField()

    def __str__(self):
        return self.itemname