# Generated by Django 4.1.2 on 2023-01-06 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_remove_cabinets_hard_cabinets_harware_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabinets',
            old_name='harware_name',
            new_name='hardware_name',
        ),
    ]
