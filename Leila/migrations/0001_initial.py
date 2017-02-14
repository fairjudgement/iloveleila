# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('yaratilma_tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayinlanma_tarihi', models.DateTimeField(blank=True, null=True)),
                ('yazar', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
