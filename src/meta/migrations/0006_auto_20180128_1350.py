# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0005_auto_20180127_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schema',
            old_name='schema_spec',
            new_name='specification',
        ),
        migrations.RemoveField(
            model_name='schema',
            name='types_spec',
        ),
    ]
