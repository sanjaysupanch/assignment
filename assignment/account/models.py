import pytz
from django.db import models
from timezone_field import TimeZoneField
from datetime import datetime


class Member(models.Model):
   mid = models.CharField(max_length=12, unique=True)
   real_name = models.CharField(max_length=60)
   TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
   tz = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
   # tz = TimeZoneField()

class Period(models.Model):
   member = models.ForeignKey(Member, related_name='activity_periods', on_delete=models.CASCADE)
   start = models.DateTimeField()
   end = models.DateTimeField()