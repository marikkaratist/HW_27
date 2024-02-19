# Generated by Django 5.0.2 on 2024-02-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
