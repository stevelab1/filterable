# Generated by Django 3.1.5 on 2021-01-13 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='subgenres',
            new_name='sub',
        ),
    ]
