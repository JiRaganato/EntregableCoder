# Generated by Django 4.0.5 on 2022-06-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='familiar',
            field=models.CharField(default='familiar', max_length=20),
        ),
        migrations.AlterField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(default='preguntar'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(default='preguntar', max_length=30),
        ),
    ]
