# Generated by Django 3.2.9 on 2021-11-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vriti_app', '0007_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]