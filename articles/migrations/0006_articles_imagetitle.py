# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160702_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='imageTitle',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
