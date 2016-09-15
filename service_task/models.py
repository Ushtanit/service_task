from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class SiteInfo(models.Model):
    url = models.TextField(max_length=2048)
    title = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(default=now)
