from django.db import models

# Create your models here.


class Light(models.Model):
    light_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    status = models.BooleanField(default=False)

    def get_status_display(self):
        if self.status:
            return "On"
        else:
            return "Off"


class Thermostat(models.Model):
    thermostat_name = models.CharField(max_length=30)



class Speaker(models.Model):
    speaker_name = models.CharField(max_length=30)


class SecurityCamera(models.Model):
    camera_name = models.CharField(max_length=30)



class Television(models.Model):
    tv_name = models.CharField(max_length=30)