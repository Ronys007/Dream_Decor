# Generated by Django 3.0.5 on 2022-10-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20221006_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
