# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pic',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='gallery/'),
            preserve_default=False,
        ),
    ]
