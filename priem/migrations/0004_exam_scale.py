# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('priem', '0003_speciality'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_scale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_form', models.SmallIntegerField(default=0)),
                ('ball_3', models.IntegerField(default=0)),
                ('ball_4', models.IntegerField(default=0)),
                ('ball_5', models.IntegerField(default=0)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priem.Discipline')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='priem.Speciality')),
            ],
        ),
    ]
