from django.db import models


class Apartments(models.Model):
    name = models.CharField(max_length=50, blank=False)


class PriceInfo(models.Model):
    apart = models.ForeignKey(Apartments, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, default=0)
