
import os.path
from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
import datetime


# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    def filepath(self, filename):
        old_filename = filename
        time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
        filename = "%s%s" % (time_now, old_filename)
        return os.path.join("uploads/", filename)

    car_title = models.CharField(max_length=100)
    price = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(choices=state_choice, max_length=100)
    color = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    year = models.IntegerField()
    description = RichTextField()
    car_image = models.ImageField(upload_to=filepath)
    car_image_1 = models.ImageField(upload_to=filepath)
    car_image_2 = models.ImageField(upload_to=filepath)
    car_image_3 = models.ImageField(upload_to=filepath)
    car_image_4 = models.ImageField(upload_to=filepath)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    exaterion = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=100)
    passenger = models.IntegerField()
    vin_number = models.CharField(max_length=100)
    milage = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    no_of_owner = models.IntegerField()
    warranty = models.IntegerField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.car_title}"

