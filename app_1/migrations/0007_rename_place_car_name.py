# Generated by Django 4.1.3 on 2022-11-16 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0006_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='place',
            new_name='name',
        ),
    ]
