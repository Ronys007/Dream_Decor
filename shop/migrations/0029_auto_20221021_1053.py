# Generated by Django 3.0.5 on 2022-10-21 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0028_auto_20221021_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='user', max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default=1, max_length=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='USA', max_length=100),
        ),
    ]
