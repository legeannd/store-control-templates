from django.db import models

class Product(models.Model):
  title = models.CharField(max_length=50, default='')
  quantity = models.IntegerField()
  description = models.TextField(max_length=200, default='')
  value = models.FloatField()
  barcode = models.CharField(max_length=50, default='')