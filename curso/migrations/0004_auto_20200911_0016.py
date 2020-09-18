# Generated by Django 3.0.3 on 2020-09-11 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_auto_20200910_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='curso',
            name='generacion',
        ),
        migrations.AddField(
            model_name='curso',
            name='numero_g',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Generacion'),
        ),
    ]