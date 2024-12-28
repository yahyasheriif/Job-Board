# Generated by Django 4.2.11 on 2024-12-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='punlished_at',
            new_name='published_at',
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to='jobs/%y/%m/%d'),
        ),
    ]