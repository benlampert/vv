# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0002_auto_20141230_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='for_marketing',
            field=models.BooleanField(default=0, verbose_name=b'For Marketing'),
            preserve_default=True,
        ),
    ]
