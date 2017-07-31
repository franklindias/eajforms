# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-31 00:52
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome da turma')),
                ('start_at', models.DateField()),
                ('end_at', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Turmas',
                'verbose_name': 'Turma',
            },
        ),
        migrations.CreateModel(
            name='CoordinatorCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Ativado'), (2, 'Desativado')])),
                ('create_at', models.DateField(auto_now=True, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name_plural': 'Coordenadores de Curso',
                'verbose_name': 'Coordenador de Curso',
            },
        ),
        migrations.CreateModel(
            name='CoordinatorPole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Ativado'), (2, 'Desativado')])),
                ('create_at', models.DateField(auto_now=True, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name_plural': 'Coordenadores de Polo',
                'verbose_name': 'Coordenador de Polo',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='CoursePole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
            ],
            options={
                'verbose_name_plural': 'Cursos do Polo',
                'verbose_name': 'Curso do Polo',
            },
        ),
        migrations.CreateModel(
            name='DocenteCoursePole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Ativado'), (2, 'Desativado')])),
                ('type_docente', models.PositiveIntegerField(choices=[(1, 'Professor'), (2, 'Professor Pesquisador'), (3, 'Professor Mediador'), (4, 'Tutor Presencial'), (5, 'Tutor EAD')], default=1)),
                ('course_pole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CoursePole')),
            ],
            options={
                'verbose_name_plural': 'Docentes em um curso',
                'verbose_name': 'Docente em um curso',
            },
        ),
        migrations.CreateModel(
            name='Matriculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matriculation', models.CharField(blank=True, max_length=30, null=True)),
                ('situation', models.PositiveIntegerField(choices=[(1, 'Matriculado'), (2, 'Jubilado'), (3, 'Trancado'), (4, 'Finalizado')], default=1, verbose_name='Situação da Matrícula')),
                ('class_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ClassCourse')),
            ],
            options={
                'verbose_name_plural': 'Matrículas',
                'verbose_name': 'Matrícula',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=20, null=True, unique=True)),
                ('full_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Pessoas',
                'verbose_name': 'Pessoa',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Polos',
                'verbose_name': 'Polo',
            },
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person')),
            ],
            options={
                'verbose_name_plural': 'docentes',
                'verbose_name': 'docente',
            },
            bases=('core.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Person')),
                ('is_egress', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Alunos',
                'verbose_name': 'Aluno',
            },
            bases=('core.person',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='coursepole',
            name='pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pole'),
        ),
        migrations.AddField(
            model_name='coordinatorpole',
            name='pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pole'),
        ),
        migrations.AddField(
            model_name='coordinatorcourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course'),
        ),
        migrations.AddField(
            model_name='classcourse',
            name='course_pole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CoursePole'),
        ),
        migrations.AddField(
            model_name='matriculation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Student'),
        ),
        migrations.AddField(
            model_name='docentecoursepole',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Docente'),
        ),
        migrations.AddField(
            model_name='coordinatorpole',
            name='docente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Docente'),
        ),
        migrations.AddField(
            model_name='coordinatorcourse',
            name='docente',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Docente'),
        ),
    ]
