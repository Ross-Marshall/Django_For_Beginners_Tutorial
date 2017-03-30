from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
     artist = models.charfield(max.length=250)
     album_title = 
