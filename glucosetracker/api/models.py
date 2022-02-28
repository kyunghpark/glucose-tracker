from django.db import models


class GlucoseReading(models.Model):
    user_id = models.CharField(max_length=255, null=True)
    device_name = models.CharField(max_length=255, null=True)
    device_serial = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(null=True)
    recording_type = models.IntegerField(null=True)
    glucose_level = models.IntegerField(null=True)
