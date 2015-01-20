# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0035_auto_20150118_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deal_name', models.CharField(max_length=200)),
                ('deal_ID_input', models.CharField(max_length=200)),
                ('price_q1', models.FloatField(default=0.0)),
                ('price_q2', models.FloatField(default=0.0)),
                ('price_q3', models.FloatField(default=0.0)),
                ('price_q4', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'Deal',
                'verbose_name_plural': 'Deals',
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='deals',
            name='deal_type',
            field=models.ForeignKey(related_name='deal_types', to='deals.DealTypes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deals',
            name='integrated_conduit',
            field=models.ForeignKey(related_name='conduit', to='vendors.Inventory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deals',
            name='integrated_dsp',
            field=models.ForeignKey(related_name='dsp', to='vendors.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deals',
            name='price_model',
            field=models.ForeignKey(related_name='price_models', to='deals.PriceModels'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deals',
            name='site_name',
            field=models.ForeignKey(related_name='deal_site', to='deals.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deals',
            name='size',
            field=models.ForeignKey(related_name='sizes', to='deals.Size'),
            preserve_default=True,
        ),
    ]
