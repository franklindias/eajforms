# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-29 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pole_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
                ('pole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pole')),
            ],
            options={
                'verbose_name_plural': 'Turmas',
                'verbose_name': 'Turma',
            },
        ),
        migrations.RemoveField(
            model_name='person',
            name='matriculation_number',
        ),
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
