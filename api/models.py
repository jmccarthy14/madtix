from django.db import models
import datetime

class Ticket(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    pickup_location = models.CharField(max_length=255, null=True)
    seller_email_address = models.EmailField(null=True)
    seller_phone = models.CharField(max_length=20, null=True)
    external_src = models.CharField(max_length=100, null=True)
    external_listing_url = models.URLField(null=True)
    created = models.DateTimeField(default=datetime.datetime.now,auto_now_add=True)
    updated = models.DateTimeField(default=datetime.datetime.now, auto_now=True)

class CLListing(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024)
    link = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    location = models.CharField(max_length=1024, null=True)
    email = models.CharField(max_length=1024, null=True)
    phone = models.CharField(max_length=1024, null=True)
    created = models.DateTimeField(default=datetime.datetime.now,auto_now_add=True)
    updated = models.DateTimeField(default=datetime.datetime.now,auto_now=True)

