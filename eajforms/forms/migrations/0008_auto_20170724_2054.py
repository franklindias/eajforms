# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-24 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_remove_form_type_evaluated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternative',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
