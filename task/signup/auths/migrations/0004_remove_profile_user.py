# Generated by Django 3.1.1 on 2020-09-17 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0003_auto_20200918_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
