# Generated by Django 2.2.17 on 2021-01-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmark',
            name='mark',
            field=models.PositiveSmallIntegerField(),
        ),
    ]