# Generated by Django 4.0.3 on 2022-08-10 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autentication', '0002_remove_task_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]
