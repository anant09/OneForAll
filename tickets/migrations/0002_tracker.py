# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-29 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('courier_details', models.BigIntegerField()),
            ],
        ),
    ]
