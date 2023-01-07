# Generated by Django 4.1.2 on 2023-01-06 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0009_cabinets_hardware_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_name', models.TextField(unique=True)),
                ('hardware_number', models.TextField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cabinets',
            name='hard',
        ),
        migrations.RemoveField(
            model_name='cabinets',
            name='hardware_number',
        ),
        migrations.AddField(
            model_name='cabinets',
            name='hardware',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='list.hardware'),
        ),
    ]