# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(default=None, max_length=50)),
                ('lastname', models.CharField(default=None, max_length=50)),
                ('username', models.CharField(unique=True, max_length=20)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(unique=True, max_length=15)),
                ('address', models.CharField(max_length=500)),
                ('registered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Query', models.CharField(max_length=400)),
                ('User_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otp', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('salonId', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(default=None, max_length=50)),
                ('image', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalonBranch',
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
        migrations.CreateModel(
            name='SalonDetailsComboDeals_1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Haircut_and_more', models.CharField(max_length=20)),
                ('Facial_and_Detan', models.CharField(max_length=20)),
                ('Bridal_packages', models.CharField(max_length=20)),
                ('BodyMassage_and_steambath', models.CharField(max_length=20)),
                ('HeadMassage_and_conditioning', models.CharField(max_length=20)),
                ('branchId', models.ForeignKey(to='Styles_app.SalonBranch')),
            ],
        ),
        migrations.CreateModel(
            name='SalonDetailsSingleDeals_1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Haircut', models.CharField(max_length=20)),
                ('Trimming', models.CharField(max_length=20)),
                ('Shave', models.CharField(max_length=20)),
                ('BodyMassage', models.CharField(max_length=20)),
                ('HeadMassage', models.CharField(max_length=20)),
                ('Bleach', models.CharField(max_length=20)),
                ('Facial', models.CharField(max_length=20)),
                ('branchId', models.ForeignKey(to='Styles_app.SalonBranch')),
            ],
        ),
    ]
