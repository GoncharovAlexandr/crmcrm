# Generated by Django 4.1.7 on 2023-08-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_remove_taskfile_file_remove_taskfile_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskfile',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='task_files/'),
        ),
        migrations.AddField(
            model_name='taskfile',
            name='task',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crm.task'),
            preserve_default=False,
        ),
    ]
