# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0047_auto_20150204_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deal_type_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Deal Type',
                'verbose_name_plural': 'Deal Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IabMainCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iab_main_category_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'IAB Main Category',
                'verbose_name_plural': 'IAB Main Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IabSubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iab_sub_category_name', models.CharField(max_length=200)),
                ('iab_main_category', models.ForeignKey(related_name='iab_main_category', to='deals.IabMainCategory')),
            ],
            options={
                'verbose_name': 'IAB Sub Category',
                'verbose_name_plural': 'IAB Sub Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceModels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_model_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Price Model',
                'verbose_name_plural': 'Price Models',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publisher_name', models.CharField(max_length=200)),
                ('integrated_conduits', models.ManyToManyField(to='vendors.Inventory')),
            ],
            options={
                'verbose_name': 'Publishers',
                'verbose_name_plural': 'Publishers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=200)),
                ('aod_wide_deals', models.BooleanField(default=0, verbose_name=b'AOD-wide Deals Available')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='site',
            name='available_sizes',
            field=models.ManyToManyField(to='deals.Size'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='iab_category',
            field=models.ManyToManyField(to='deals.IabMainCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='publisher',
            field=models.ForeignKey(related_name='publisher', to='deals.Publisher'),
            preserve_default=True,
        ),
    ]
