# Generated by Django 4.2.11 on 2024-12-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0017_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='<function-Job.__str__-at-0x72a2cd34d1c0>'),
        ),
    ]
