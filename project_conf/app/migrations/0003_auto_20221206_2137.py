# Generated by Django 3.0 on 2022-12-07 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221206_2136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='cfm',
            new_name='crm',
        ),
    ]
