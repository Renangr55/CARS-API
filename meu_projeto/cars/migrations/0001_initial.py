# Generated by Django 5.1.6 on 2025-02-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('model_year', models.IntegerField()),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
