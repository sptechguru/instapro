# Generated by Django 2.2.11 on 2020-07-08 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='first_name',
        ),
    ]
