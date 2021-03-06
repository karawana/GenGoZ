# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0022_auto_20160510_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='exam_date',
            field=models.DateField(default='2016-05-12'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='statistics',
            unique_together=set([('user', 'book', 'type', 'step', 'status', 'exam_date')]),
        ),
    ]
