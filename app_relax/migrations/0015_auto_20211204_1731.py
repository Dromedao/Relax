# Generated by Django 3.0 on 2021-12-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0014_auto_20211201_1901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='sms',
        ),
        migrations.AddField(
            model_name='dog',
            name='fecha',
            field=models.CharField(default='2021-12-04', max_length=200),
        ),
    ]
