# Generated by Django 5.0.2 on 2024-02-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
