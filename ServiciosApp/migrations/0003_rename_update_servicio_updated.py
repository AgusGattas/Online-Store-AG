# Generated by Django 4.1 on 2022-09-20 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0002_alter_servicio_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='update',
            new_name='updated',
        ),
    ]
