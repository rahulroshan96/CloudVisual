# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth

class Credentials(models.Model):
    credential_name = models.CharField(max_length=40, unique=True)
    client_id = models.CharField(max_length=40)
    secret_key = models.CharField(max_length=50)
    tenant_id = models.CharField(max_length=40)
    subscription_id = models.CharField(max_length=40)
    bearer_token = models.CharField(max_length=2000, default='0')
    token_expire_on = models.CharField(max_length=15, default='0')
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    social_user = models.ForeignKey(UserSocialAuth, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.credential_name


