# Generated by Django 3.0.5 on 2022-11-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_auto_20221025_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Invoice',
            field=models.URLField(blank=True, max_length=2000),
        ),
    ]
