# Generated by Django 3.0 on 2021-12-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0036_auto_20211207_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='intensidad',
            new_name='intensity',
        ),
        migrations.AlterField(
            model_name='nota',
            name='timestamp',
            field=models.DateTimeField(default='2021-12-07 17:47'),
        ),
    ]
