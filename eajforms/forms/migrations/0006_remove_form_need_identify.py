# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-20 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20170720_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='need_identify',
        ),
    ]
