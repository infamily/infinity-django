# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-12 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_cryptokeypair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptokeypair',
            name='type',
            field=models.PositiveSmallIntegerField(default=1, verbose_name=[(0, 'None'), (1, 'IPDB')]),
        ),
    ]
