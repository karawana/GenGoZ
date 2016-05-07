# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20160507_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='type',
            field=models.CharField(choices=[('w', 'Word'), ('m', 'Meaning')], default='w', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='statistics',
            unique_together=set([('user', 'book', 'type', 'step', 'status')]),
        ),
    ]