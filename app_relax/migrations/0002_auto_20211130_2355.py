# Generated by Django 3.0 on 2021-12-01 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
