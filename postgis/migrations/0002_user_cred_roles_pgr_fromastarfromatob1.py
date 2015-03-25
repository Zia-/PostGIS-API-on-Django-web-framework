# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_cred_roles',
            name='pgr_fromastarfromatob1',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
