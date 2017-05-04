# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Styles_app', '0006_remove_reviews_rating_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews_rating',
            name='Name',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
