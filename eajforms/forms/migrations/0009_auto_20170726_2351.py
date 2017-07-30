# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-27 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20170724_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApllyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_evaluated', models.PositiveIntegerField(choices=[(1, 'Docente'), (2, 'Coordenador'), (3, 'Curso'), (4, 'Polo')], verbose_name='Tipo de Avaliado')),
                ('login_required', models.BooleanField(default=False, verbose_name='Login é obrigatório?')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.Form')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='dont_apply',
            field=models.BooleanField(default=False, verbose_name='Não se aplica'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='forms.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='yes_no',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Concordo/Sim'), (2, 'Concordo parcialmente/Parcialmente'), (3, 'Discordo/Não')], null=True),
        ),
    ]
