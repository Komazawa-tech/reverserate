# Generated by Django 5.1.2 on 2024-11-30 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_class_group_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='code',
        ),
        migrations.RemoveField(
            model_name='group',
            name='code',
        ),
    ]
