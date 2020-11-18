# Generated by Django 3.1.3 on 2020-11-18 17:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import exiffield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Places')),
                ('default_image', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('latitud', models.CharField(editable=False, max_length=20, null=True)),
                ('longitud', models.CharField(editable=False, max_length=20, null=True)),
                ('exif', exiffield.fields.ExifField(default={}, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateField(auto_now=True)),
                ('stars', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('helpfull', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Rivable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TripAccomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TripActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('AD', 'Biking'), ('WN', 'Hiking'), ('CT', 'Running')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('AD', 'Adventure'), ('WN', 'Wildlife & Nature'), ('CT', 'Cities'), ('RU', 'Ruins & temples'), ('RT', 'Road trips'), ('HK', 'Hiking'), ('FD', 'Food & drink'), ('AC', 'Art & culture'), ('CI', 'Coasts & islans'), ('FA', 'Family')], default=None, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TripTrasnsfers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserLinked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('rivable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trip.rivable')),
            ],
            bases=('trip.rivable',),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('rivable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trip.rivable')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
            ],
            bases=('trip.rivable',),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('rivable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trip.rivable')),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('geo_json', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['geojson', 'gpx'])])),
            ],
            bases=('trip.rivable',),
        ),
    ]
