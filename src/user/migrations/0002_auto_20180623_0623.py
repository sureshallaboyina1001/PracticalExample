# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-23 06:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginsystem',
            old_name='login_time',
            new_name='user_login_time',
        ),
    ]
