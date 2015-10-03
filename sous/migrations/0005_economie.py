# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sous', '0004_depjour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economie',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('montant', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
