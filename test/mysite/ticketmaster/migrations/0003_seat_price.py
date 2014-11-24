# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0002_auto_20141124_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=1),
            preserve_default=False,
        ),
    ]
