# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-02 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_practicle_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='practicle',
            name='contributor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='practicle',
            name='contributor_url',
            field=models.URLField(default='www.google.co.in'),
        ),
    ]
