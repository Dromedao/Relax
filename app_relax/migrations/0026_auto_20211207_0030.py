# Generated by Django 3.0 on 2021-12-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0025_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='fecha',
            field=models.CharField(default='2021-12-07', max_length=200),
        ),
        migrations.AlterField(
            model_name='nota',
            name='timestamp',
            field=models.DateTimeField(default='2021-12-07 00:30'),
        ),
    ]