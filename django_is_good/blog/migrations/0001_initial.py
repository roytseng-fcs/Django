# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('create_date', models.DateTimeField(verbose_name='date published')),
                ('update_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
