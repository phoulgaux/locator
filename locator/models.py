from django.utils import timezone

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, default="", unique=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    last_sought = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        if self.latitude > 0:
            latstr = "N"
        else:
            latstr = "S"
        if self.longitude > 0:
            lonstr = "E"
        else:
            lonstr = "W"
        return u"{0} - {1}{2}, {3}{4}".format(self.name, abs(self.latitude), latstr, abs(self.longitude), lonstr)