# Generated by Django 3.0.3 on 2020-09-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200901_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='modifiedby',
            field=models.CharField(default='user', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='modifiedby',
            field=models.CharField(default='user', max_length=20),
        ),
    ]
