# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketmaster', '0003_seat_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('segmentId', models.CharField(max_length=60)),
                ('placesTotal', models.IntegerField()),
                ('placesAvailable', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
