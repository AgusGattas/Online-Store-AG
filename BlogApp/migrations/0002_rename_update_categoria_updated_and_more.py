# Generated by Django 4.1 on 2022-09-19 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='update',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update',
            new_name='updated',
        ),
    ]