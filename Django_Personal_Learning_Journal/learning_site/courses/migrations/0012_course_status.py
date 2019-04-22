# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20160121_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('i', 'In Progress'), ('r', 'In Review'), ('p', 'Published')], default='i', max_length=1),
        ),
    ]