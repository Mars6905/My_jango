# Generated by Django 5.0.1 on 2024-01-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothese',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('style', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('memory', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
