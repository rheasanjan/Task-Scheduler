# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-13 03:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
