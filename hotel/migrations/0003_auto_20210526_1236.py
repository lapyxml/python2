# Generated by Django 3.2.3 on 2021-05-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20210526_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='number_of_seats',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='occupation',
            field=models.BooleanField(default=False),
        ),
    ]
