# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-11 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181013_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]
