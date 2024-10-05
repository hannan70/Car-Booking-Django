from datetime import datetime
from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True)
    car_id = models.IntegerField()
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

    def __str__(self):
        return  self.full_name()
