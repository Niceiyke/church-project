# Generated by Django 4.2.7 on 2023-11-11 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_attendance_service_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='first_timers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='new_converts',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
