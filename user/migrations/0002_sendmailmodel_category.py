# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-01 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendmailmodel',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]