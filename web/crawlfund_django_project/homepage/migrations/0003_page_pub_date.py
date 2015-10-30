# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20151029_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 29, 18, 1, 39, 203273, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
