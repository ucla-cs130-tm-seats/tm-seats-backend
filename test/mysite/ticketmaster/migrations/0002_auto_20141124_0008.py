# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='number',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='user',
        ),
        migrations.AddField(
            model_name='seat',
            name='position',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
    ]
