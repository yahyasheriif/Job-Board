# Generated by Django 4.2.11 on 2024-12-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0016_alter_job_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='<bound-method-Field.value_from_object-of-<django.db.models.fields.CharField>>'),
        ),
    ]
