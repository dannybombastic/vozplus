# Generated by Django 2.0.7 on 2018-07-31 20:52

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180731_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menberspoint',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-4.877516799999999, 36.51584, srid=4326), srid=4326),
        ),
    ]
