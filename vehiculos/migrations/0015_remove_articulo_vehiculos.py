# Generated by Django 2.2.5 on 2019-10-11 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0014_auto_20191011_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='vehiculos',
        ),
    ]
