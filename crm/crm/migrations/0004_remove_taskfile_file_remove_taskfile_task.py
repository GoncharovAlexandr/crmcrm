# Generated by Django 4.1.7 on 2023-08-21 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskfile',
            name='file',
        ),
        migrations.RemoveField(
            model_name='taskfile',
            name='task',
        ),
    ]
