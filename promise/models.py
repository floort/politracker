from django.db import models

# Create your models here.

class Party(models.Model):
    name = models.CharField(max_length=64)
    full_name = models.CharField(max_length=256, blank=True)


class Politician(models.Model):
    name = models.CharField(max_length=128)
    party = models.ForeignKey(Party)

class Source(models.Model):
    slug = models.SlugField()
    url = models.URLField()
    date = models.DateTimeField(auto_now=True)

class Promise(models.Model):    
    slug = models.SlugField()
    title = models.CharField(max_length=128)
    open_date = models.DateTimeField(auto_now=True)
    resolved_date = models.DateTimeField()
    sources = models.ManyToManyField(Source)


