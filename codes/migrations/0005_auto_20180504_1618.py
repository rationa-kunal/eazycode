# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0004_auto_20180502_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practicle',
            name='download_all_link',
        ),
        migrations.AddField(
            model_name='practicle',
            name='language',
            field=models.CharField(choices=[('c', 'c'), ('cpp', 'c++'), ('asm6502', 'assembly')], default='c', max_length=10),
        ),
        migrations.AddField(
            model_name='subject',
            name='download_all_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='practicle',
            name='contributor_link',
            field=models.URLField(blank=True),
        ),
    ]
