# Generated by Django 4.2.11 on 2024-12-28 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0018_alter_job_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='slug',
        ),
    ]
