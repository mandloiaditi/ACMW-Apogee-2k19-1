# Generated by Django 2.1.5 on 2019-03-17 19:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_auto_20190316_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeruser',
            name='regTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 17, 19, 47, 59, 154272, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='playeruser',
            name='time',
            field=models.FloatField(default=7200.0),
        ),
    ]
