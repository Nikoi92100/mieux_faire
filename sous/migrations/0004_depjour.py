# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sous', '0003_auto_20150925_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepJour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(verbose_name='Date de la dépense', auto_now_add=True)),
            ],
        ),
    ]
