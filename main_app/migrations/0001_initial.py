# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(blank=True, null=True)),
                ('meaning', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
