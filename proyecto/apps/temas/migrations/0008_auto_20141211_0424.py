# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temas', '0007_auto_20141210_0456'),
    ]

    operations = [
        migrations.CreateModel(
            name='permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('add_tema', 'add_tema'), ('bloques_permisos', 'bloques_permisos')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='permisogeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.ForeignKey(to='temas.permiso')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='tema',
            options={},
        ),
    ]
