# Generated by Django 3.0.5 on 2022-10-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]