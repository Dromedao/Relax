# Generated by Django 3.0 on 2021-12-07 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0033_auto_20211207_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='situacion',
            new_name='situation',
        ),
        migrations.AlterField(
            model_name='nota',
            name='timestamp',
            field=models.DateTimeField(default='2021-12-07 17:41'),
        ),
    ]
