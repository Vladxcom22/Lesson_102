# Generated by Django 4.2.4 on 2023-08-31 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tittle',
            new_name='title',
        ),
    ]
