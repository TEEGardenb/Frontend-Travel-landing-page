# Generated by Django 5.0.1 on 2024-01-17 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_remove_destino_precio_destino_sada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destino',
            name='sada',
        ),
    ]