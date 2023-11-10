# Generated by Django 4.2.7 on 2023-11-10 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0002_mentors_alter_newconvert_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentors',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentors',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newconvert',
            name='date_created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newconvert',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
