# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-05 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0013_auto_20180305_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trade.Payment'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='transactions.Transaction'),
        ),
    ]