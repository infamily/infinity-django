# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-05 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20171105_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsnapshot',
            name='blockchain',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commentsnapshot',
            name='blockchain_tx',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='currencypricesnapshot',
            name='blockchain',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='currencypricesnapshot',
            name='blockchain_tx',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hourpricesnapshot',
            name='blockchain',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hourpricesnapshot',
            name='blockchain_tx',
            field=models.TextField(blank=True, null=True),
        ),
    ]
