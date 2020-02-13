# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
STATE_CHOICES = (
    ("1", "Karnataka"),
    ("2", "MadhyaPradesh"),
)

class UserInputModel(models.Model):
    user_input = models.CharField(max_length=40)


class UseDetailsModel(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    country = models.CharField(max_length=10, default='India')

    def __str__(self):
        return self.first_name