# Generated by Django 4.2.7 on 2023-11-10 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_attendance_servicetime_servicetype_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='attendance',
        ),
        migrations.AddField(
            model_name='service',
            name='attendance',
            field=models.ManyToManyField(null=True, to='management.attendance'),
        ),
    ]
