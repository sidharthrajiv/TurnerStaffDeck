from django.conf import settings
from django.db import models
from django.utils import timezone

class Self(models.Model):
    Reviews = models.TextField()

class Manager(models.Model):
    Reviews = models.TextField()

class Peer(models.Model):
    Reviews = models.TextField()

class Partner(models.Model):
    Reviews = models.TextField()
