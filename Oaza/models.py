from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)

class Reservation(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user_name = models.CharField(max_length=100)