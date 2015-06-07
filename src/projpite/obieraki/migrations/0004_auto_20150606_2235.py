# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obieraki', '0003_auto_20150605_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Mail',
            field=models.TextField(default='mail@mail.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Mail',
            field=models.TextField(default='mail@mail.com'),
            preserve_default=False,
        ),
    ]
