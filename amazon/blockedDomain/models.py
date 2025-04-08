from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField()
    domain = models.CharField(max_length=255)  # Store domain name separately

    def __str__(self):
        return self.name

class BlockedDomain(models.Model):
    domain = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.domain
