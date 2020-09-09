# Generated by Django 3.0.3 on 2020-08-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200828_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBacklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('products', models.ManyToManyField(to='dashboard.Product')),
            ],
        ),
    ]
