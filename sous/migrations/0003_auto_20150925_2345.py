# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sous', '0002_auto_20150922_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depensesfixes',
            name='montant',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='recettesfixes',
            name='montant',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
