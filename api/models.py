from django.db import models

# Create your models here.

class Ticket(models.Model):
    event = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    quantity = models.IntegerField()
    description = models.CharField(max_length=1024)
    seller_email_address = models.EmailField()
    seller_phone = models.CharField(max_length=20)
