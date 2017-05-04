# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styles_app', '0004_auto_20170503_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews_rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=400)),
                ('reviews', models.CharField(max_length=800)),
                ('branchId', models.ForeignKey(to='Styles_app.SalonBranch_1')),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews_ratings',
        ),
    ]
