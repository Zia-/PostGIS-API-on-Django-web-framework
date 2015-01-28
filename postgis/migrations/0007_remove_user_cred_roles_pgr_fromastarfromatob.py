# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postgis', '0006_user_cred_roles_session_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_cred_roles',
            name='pgr_fromastarfromatob',
        ),
    ]
