# Generated by Django 3.0.5 on 2022-10-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20221020_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
