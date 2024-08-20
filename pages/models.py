import datetime
import os.path

from django.db import models


# Create your models here.

def filepath(request, filename):
    old_filename = filename
    time_now = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (time_now, old_filename)
    return os.path.join("uploads/", filename)


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to=filepath)
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    linkedin_link = models.URLField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
