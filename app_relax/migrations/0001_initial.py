# Generated by Django 3.0 on 2021-12-01 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_buenos', models.IntegerField(default=0)),
                ('dias_decentes', models.IntegerField(default=0)),
                ('dias_normales', models.IntegerField(default=0)),
                ('dias_malos', models.IntegerField(default=0)),
                ('dias_terribles', models.IntegerField(default=0)),
                ('Como_estuvo_tu_dia', models.IntegerField(choices=[[0, 'Bueno'], [1, 'Decente'], [2, 'Normal'], [3, 'Malo'], [4, 'Terrible']], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='HowDoYouFeel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Como_estuvo_tu_dia', models.IntegerField(choices=[[0, 'Bueno'], [1, 'Decente'], [2, 'Normal'], [3, 'Malo'], [4, 'Terrible']])),
                ('algo', models.CharField(default=0, max_length=10000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='howdoyoufeel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacion', models.CharField(max_length=200)),
                ('detonante', models.CharField(default='', max_length=200)),
                ('sentimiento', models.IntegerField(choices=[[0, 'Tristeza'], [1, 'Rabia'], [2, 'Angustia'], [3, 'Ansia'], [4, 'Miedo'], [5, 'Frustración'], [6, 'Verguenza']], default=2)),
                ('intensidad', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formulario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.CharField(default='', max_length=200)),
                ('nombre', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Perro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
