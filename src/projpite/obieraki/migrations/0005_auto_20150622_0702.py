# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obieraki', '0004_auto_20150606_2235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_2',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='Surname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Surname',
        ),
        migrations.AlterField(
            model_name='course',
            name='Name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Department',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Mail',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Title',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='FieldOfStudy',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='Mail',
            field=models.TextField(max_length=30),
        ),
    ]
