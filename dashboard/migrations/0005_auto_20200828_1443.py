# Generated by Django 3.0.3 on 2020-08-28 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_productbacklog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Colours'),
        ),
    ]
