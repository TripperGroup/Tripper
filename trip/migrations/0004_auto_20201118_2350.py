# Generated by Django 3.1.3 on 2020-11-18 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_remove_image_exif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
