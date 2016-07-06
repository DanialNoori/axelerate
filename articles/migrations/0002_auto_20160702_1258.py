# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 09:28
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('datePublished', models.TextField()),
                ('viewCount', models.IntegerField()),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
