# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 17:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0022_auto_20180326_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-id'], 'permissions': (('change_creators', 'Can change the creators for entries'),), 'verbose_name_plural': 'entries'},
        ),
    ]
