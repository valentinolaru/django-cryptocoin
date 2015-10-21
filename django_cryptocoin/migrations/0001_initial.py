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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('currency', models.CharField(choices=[('nvc', 'Novacoin'), ('emc', 'Emercoin'), ('btc', 'Bitcoin'), ('ltc', 'Litecoin')], max_length=50, default='btc')),
                ('addr', models.CharField(max_length=50)),
                ('amount', models.DecimalField(max_digits=18, decimal_places=8)),
                ('amount_received', models.DecimalField(max_digits=18, decimal_places=8, default=0)),
                ('amount_received_confirmed', models.DecimalField(max_digits=18, decimal_places=8, default=0)),
                ('redirect_to', models.CharField(max_length=200, default='/')),
                ('date', models.DateTimeField()),
                ('processed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('currency1', models.CharField(max_length=50, default='btc')),
                ('currency2', models.CharField(max_length=50, default='usd')),
                ('rate', models.DecimalField(max_digits=18, decimal_places=8, default=0)),
            ],
        ),
    ]
