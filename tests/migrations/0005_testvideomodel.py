# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 08:31
from __future__ import unicode_literals

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20160806_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestVideoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='tests-videos/')),
            ],
        ),
    ]
