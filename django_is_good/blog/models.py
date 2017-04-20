# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=500) 
   slug = models.SlugField()
   body = models.TextField()
   create_date = models.DateTimeField('date published')
   update_date = models.DateTimeField('date created')
