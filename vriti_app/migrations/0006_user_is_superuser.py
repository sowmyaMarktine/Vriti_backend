# Generated by Django 3.2.9 on 2021-11-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vriti_app', '0005_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]