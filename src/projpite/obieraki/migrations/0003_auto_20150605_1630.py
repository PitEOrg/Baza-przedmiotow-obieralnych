# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obieraki', '0002_auto_20150605_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='User_2_idUser_2',
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
