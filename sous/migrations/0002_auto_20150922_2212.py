# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sous', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recettesfixes',
            old_name='monant',
            new_name='montant',
        ),
    ]
