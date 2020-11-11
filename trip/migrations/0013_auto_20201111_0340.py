# Generated by Django 3.1.2 on 2020-11-11 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0012_auto_20201103_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='tripplaces',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='places', to='trip.trip'),
        ),
    ]
