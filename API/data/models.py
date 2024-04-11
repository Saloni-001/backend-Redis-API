from django.db import models
from django.db import models

class DeviceData(models.Model):
    device_fk_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_stamp = models.DateTimeField()
    sts = models.DateTimeField()
    speed = models.FloatField()
