# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-12 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('todo_id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=300)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('resolve_time', models.DateTimeField()),
                ('status', models.CharField(default='No', max_length=4)),
            ],
            options={
                'ordering': ['add_time', 'status'],
            },
        ),
    ]