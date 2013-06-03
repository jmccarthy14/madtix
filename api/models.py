from django.db import models


class Ticket(models.Model):
    event = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1024)
    seller_email_address = models.EmailField()
    seller_phone = models.CharField(max_length=20)
    external_src = models.CharField(max_length=100)
    external_listing_url = models.URLField()


class CLListing(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    link = models.CharField(max_length=1024)
    price = models.CharField(max_length=1024, null=True)
    location = models.CharField(max_length=1024, null=True)
    email = models.CharField(max_length=1024, null=True)
    phone = models.CharField(max_length=1024, null=True)

