# Generated by Django 3.0.3 on 2020-09-10 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
                ('generacion', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Curso',
            },
        ),
    ]
