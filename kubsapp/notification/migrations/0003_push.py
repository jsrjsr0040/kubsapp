# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-17 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20180217_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('push_author', models.IntegerField(default=0)),
                ('push_title', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
