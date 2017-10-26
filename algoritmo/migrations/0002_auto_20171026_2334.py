# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('algoritmo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='combinaciones',
            options={'verbose_name_plural': 'Combinaciones', 'managed': True},
        ),
    ]
