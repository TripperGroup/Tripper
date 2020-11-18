# Generated by Django 3.1.3 on 2020-11-18 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlinked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='rivable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.rivable'),
        ),
        migrations.AddField(
            model_name='image',
            name='rivable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='trip.rivable'),
        ),
        migrations.AddField(
            model_name='companions',
            name='companion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userlinked',
            name='liked_trips',
            field=models.ManyToManyField(blank=True, related_name='likedtrips', to='trip.Trip'),
        ),
        migrations.AddField(
            model_name='userlinked',
            name='saved_places',
            field=models.ManyToManyField(blank=True, related_name='savedplaces', to='trip.Place'),
        ),
        migrations.AddField(
            model_name='userlinked',
            name='saved_trips',
            field=models.ManyToManyField(blank=True, related_name='savedtrips', to='trip.Trip'),
        ),
        migrations.AddField(
            model_name='tripplaces',
            name='places',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='trip.place'),
        ),
        migrations.AddField(
            model_name='tripplaces',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='places', to='trip.trip'),
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
        migrations.AddField(
            model_name='companions',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trip.trip'),
        ),
    ]