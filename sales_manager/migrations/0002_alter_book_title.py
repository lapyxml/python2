# Generated by Django 3.2.3 on 2021-05-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(db_index=True, max_length=100, verbose_name='название'),
        ),
    ]
