# Generated by Django 4.1 on 2022-09-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiciosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]