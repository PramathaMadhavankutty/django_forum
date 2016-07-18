from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings

# Create your models here.
class Subject(models.Model):

    name = models.CharField(max_length=255)
    description = HTMLField()

    def __unicode__(self):
        return self.name
