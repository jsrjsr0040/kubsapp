# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20180129_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
