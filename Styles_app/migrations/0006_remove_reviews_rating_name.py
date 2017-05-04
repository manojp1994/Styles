# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styles_app', '0005_auto_20170503_2349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews_rating',
            name='Name',
        ),
    ]
