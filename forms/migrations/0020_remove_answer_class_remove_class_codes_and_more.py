# Generated by Django 5.1.2 on 2024-12-31 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0019_code_day_of_week_field_period_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='class',
            name='codes',
        ),
        migrations.RemoveField(
            model_name='class',
            name='days_of_week',
        ),
        migrations.RemoveField(
            model_name='class',
            name='fields',
        ),
        migrations.RemoveField(
            model_name='class',
            name='period',
        ),
        migrations.RemoveField(
            model_name='class',
            name='semester',
        ),
        migrations.DeleteModel(
            name='group',
        ),
        migrations.DeleteModel(
            name='TestModel',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='code',
        ),
        migrations.DeleteModel(
            name='day_of_week',
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='period',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='semester',
        ),
    ]
