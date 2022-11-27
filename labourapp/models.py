from django.db import models

# Create your models here.
class sub(models.Model):
    name=models.CharField( max_length=100)
    contact=models.CharField( max_length=12)
    password=models.CharField( max_length=16)
    street_name=models.CharField( max_length=100)
    police_station=models.CharField( max_length=100)
    city=models.CharField( max_length=100)
    state=models.CharField( max_length=100)
    pin=models.CharField( max_length=8)
    work=models.CharField( max_length=100)
    def __str__(self):
        return self.name