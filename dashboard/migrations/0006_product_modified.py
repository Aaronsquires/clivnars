# Generated by Django 3.0.3 on 2020-08-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200828_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
