# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 23:47
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0004_auto_20180213_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('processor', models.PositiveSmallIntegerField(default=1)),
                ('hours', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=8, default=0.0, max_digits=20)),
                ('platform', models.CharField(default='stripe', max_length=20)),
                ('provider', models.CharField(default='card', max_length=20)),
                ('reqeust', django.contrib.postgres.fields.jsonb.JSONField()),
                ('response', django.contrib.postgres.fields.jsonb.JSONField()),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='transactions.Currency')),
                ('currency_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_prices', to='transactions.CurrencyPriceSnapshot')),
                ('hour_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hour_prices', to='transactions.HourPriceSnapshot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
