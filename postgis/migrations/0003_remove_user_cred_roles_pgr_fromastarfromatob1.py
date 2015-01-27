# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0002_user_cred_roles_pgr_fromastarfromatob1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_cred_roles',
            name='pgr_fromastarfromatob1',
        ),
    ]
