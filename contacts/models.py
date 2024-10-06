from datetime import datetime
from django.db import models
from cars.models import Car

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True)
    car_title = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    customer_needs = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    messages = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def car_address(self):
        return f"{self.state}, {self.city}"

    def __str__(self):
        return  self.full_name()
