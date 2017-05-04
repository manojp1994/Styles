# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styles_app', '0002_auto_20170425_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalonBranch_1',
            fields=[
                ('branchId', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True, blank=True)),
                ('branchLocation', models.CharField(default=None, max_length=20)),
                ('address', models.CharField(default=None, max_length=50)),
                ('contactnumber', models.CharField(unique=True, max_length=20)),
                ('servicetype', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=500, null=True)),
                ('salonId', models.ForeignKey(to='Styles_app.Salon')),
            ],
        ),
        migrations.RemoveField(
            model_name='salonbranch',
            name='salonId',
        ),
        migrations.AlterField(
            model_name='salondetailscombodeals_1',
            name='branchId',
            field=models.ForeignKey(to='Styles_app.SalonBranch_1'),
        ),
        migrations.AlterField(
            model_name='salondetailssingledeals_1',
            name='branchId',
            field=models.ForeignKey(to='Styles_app.SalonBranch_1'),
        ),
        migrations.DeleteModel(
            name='SalonBranch',
        ),
    ]
