# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=200)),
                ('aod_wide_deals', models.BooleanField(default=0, verbose_name=b'AOD-wide Deals Available')),
                ('price_range_min', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('price_range_max', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('site_internal_pov', models.TextField(default=b'empty', max_length=1000, verbose_name=b'Internal POV')),
                ('available_sizes', models.ManyToManyField(to='deals.Size')),
                ('iab_category', models.ForeignKey(to='deals.IabMainCategory')),
                ('publisher', models.ForeignKey(related_name='parent_publisher', to='deals.Publisher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
