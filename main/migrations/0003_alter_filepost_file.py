# Generated by Django 4.1.4 on 2023-01-27 20:58

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_filepost_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filepost',
            name='file',
            field=models.FileField(upload_to=main.models.get_upload_to),
        ),
    ]
