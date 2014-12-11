# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_auto_20141202_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='idSa',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='idUs',
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='idUs',
        ),
        migrations.DeleteModel(
            name='Sala',
        ),
    ]
