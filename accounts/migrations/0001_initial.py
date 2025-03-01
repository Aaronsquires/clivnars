# Generated by Django 3.0.3 on 2020-08-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
    ]
