# Generated by Django 3.0 on 2021-12-04 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_relax', '0016_auto_20211204_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='content',
        ),
    ]
