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
            name='price',
        ),
        migrations.AddField(
            model_name='segment',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=1),
            preserve_default=False,
        ),
    ]
