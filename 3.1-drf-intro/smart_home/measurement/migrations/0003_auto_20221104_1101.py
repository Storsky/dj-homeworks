# Generated by Django 3.1.2 on 2022-11-04 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_auto_20221104_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='sensor_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='measeurements', to='measurement.sensor'),
            preserve_default=False,
        ),
    ]
