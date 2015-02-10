# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0009_auto_20150128_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id_user', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
