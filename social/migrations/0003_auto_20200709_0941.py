# Generated by Django 2.2.11 on 2020-07-09 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_remove_myprofile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]