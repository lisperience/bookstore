# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20151126_0006'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('name', 'lastname')]),
        ),
    ]
