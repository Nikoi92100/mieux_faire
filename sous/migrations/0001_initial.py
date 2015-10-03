# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepensesFixes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titre', models.CharField(max_length=50)),
                ('montant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecettesFixes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titre', models.CharField(max_length=50)),
                ('monant', models.CharField(max_length=100)),
            ],
        ),
    ]
