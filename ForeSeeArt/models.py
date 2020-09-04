import datetime

from django.db import models
from django.utils import timezone

class Exhibit(models.Model):
    exhibit_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, )
    venue = models.ForeignKey(Venue), )
    exhibit_start_date = models.DateTimeField('start date')
    exhibit_end_date = models.DateTimeField('end date')

"""
    def __str__(self):
        return self.exhibit_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
"""

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

    def __str__(self):
        return self.artist_name

class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    venue_street_address = models.CharField(max_length=200)
    venue_city = models.CharField(max_length=50)
    venue_state_province = models.CharField(max_length=20)
    venue_postal = models.CharField(max_length=15)
    venue_country = models.CharField(max_length=100)
    venue_web_site = models.CharField(max_length=200)

    def __str__(self):
        return self.venue_name
