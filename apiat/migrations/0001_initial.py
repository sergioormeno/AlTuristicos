# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('nombre', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('nombre', models.TextField(null=True, blank=True)),
                ('direccion', models.TextField(null=True, blank=True)),
                ('num_dir', models.TextField(null=True, blank=True)),
                ('telefono', models.TextField(null=True, blank=True)),
                ('clase', models.TextField(null=True, blank=True)),
                ('web', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'establecimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('nombre', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'provincia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, blank=True)),
                ('nombre', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
