# Generated by Django 5.0.2 on 2024-02-17 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]