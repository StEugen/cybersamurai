# Generated by Django 4.1.2 on 2023-01-06 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0011_hardware_cabinet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabinets',
            name='hardware',
        ),
    ]
