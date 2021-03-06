# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-11 21:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_auto_20190111_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credential_name', models.CharField(max_length=40)),
                ('client_id', models.CharField(max_length=40)),
                ('secret_key', models.CharField(max_length=40)),
                ('tenant_id', models.CharField(max_length=40)),
                ('subscription_id', models.CharField(max_length=40)),
                ('bearer_token', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='employe',
            name='boss',
        ),
        migrations.RemoveField(
            model_name='employe',
            name='job',
        ),
        migrations.DeleteModel(
            name='Employe',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
