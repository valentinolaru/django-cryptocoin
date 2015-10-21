# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('currency', models.CharField(choices=[('btc', 'Bitcoin'), ('ltc', 'Litecoin'), ('nvc', 'Novacoin'), ('emc', 'Emercoin')], max_length=50, default='btc')),
                ('addr', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=18)),
                ('amount_received', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
                ('amount_received_confirmed', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
                ('redirect_to', models.CharField(max_length=200, default='/')),
                ('date', models.DateTimeField()),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('currency1', models.CharField(max_length=50, default='btc')),
                ('currency2', models.CharField(max_length=50, default='usd')),
                ('rate', models.DecimalField(decimal_places=8, default=0, max_digits=18)),
            ],
        ),
    ]
