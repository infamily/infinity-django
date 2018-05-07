# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-07 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20180201_1848'),
        ('trade', '0014_auto_20180305_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Topic'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Topic'),
        ),
    ]