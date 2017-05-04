# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styles_app', '0003_auto_20170425_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews_ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=400)),
                ('reviews', models.CharField(max_length=800)),
            ],
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.ImageField(default=1, upload_to=b'image'),
            preserve_default=False,
        ),
    ]
