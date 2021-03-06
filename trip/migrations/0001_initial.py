# Generated by Django 3.1.3 on 2020-11-26 16:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('geo_json', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['geojson', 'gpx'])])),
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
            name='UserLinked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_trips', models.ManyToManyField(blank=True, related_name='likedtrips', to='trip.Trip')),
                ('saved_places', models.ManyToManyField(blank=True, related_name='savedplaces', to='trip.Place')),
                ('saved_trips', models.ManyToManyField(blank=True, related_name='savedtrips', to='trip.Trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('stars', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('helpfull', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.place')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='places', to='trip.trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Places')),
                ('default_image', models.BooleanField(default=False)),
                ('subject', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('latitud', models.CharField(editable=False, max_length=20, null=True)),
                ('longitud', models.CharField(editable=False, max_length=20, null=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='trip.trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='activities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trip.tripactivities'),
        ),
        migrations.AddField(
            model_name='trip',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='category',
            field=models.ManyToManyField(blank=True, to='trip.TripCategory'),
        ),
        migrations.CreateModel(
            name='Companions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip')),
            ],
        ),
    ]
