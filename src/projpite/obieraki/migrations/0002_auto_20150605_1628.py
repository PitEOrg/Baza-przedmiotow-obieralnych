# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obieraki', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='Instructor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='Hours',
        ),
        migrations.RemoveField(
            model_name='course',
            name='ID_NO',
        ),
        migrations.RemoveField(
            model_name='student',
            name='User_2_idUser_2',
        ),
        migrations.RemoveField(
            model_name='user_2',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='user_2',
            name='Surname',
        ),
        migrations.AddField(
            model_name='course',
            name='Exam',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='Requirements',
            field=models.TextField(default='Requirements'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='WayOfGettingCredit',
            field=models.TextField(default='Way of getting credit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Name',
            field=models.TextField(default='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='Surname',
            field=models.TextField(default='Surname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='CollectedECTS',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Name',
            field=models.TextField(default='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Surname',
            field=models.TextField(default='Surname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Staff_idStaff',
            field=models.ForeignKey(to='obieraki.Staff'),
        ),
    ]
