# Generated by Django 5.1.2 on 2024-12-19 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0002_delete_testmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='codes',
            new_name='code',
        ),
    ]
