# Generated by Django 3.0.3 on 2020-08-27 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=30)),
                ('colourcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default='1')),
                ('minquantity', models.IntegerField(default='5')),
                ('colour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Colours')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Supplier')),
            ],
        ),
    ]
