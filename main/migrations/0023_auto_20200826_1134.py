# Generated by Django 3.1 on 2020-08-26 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200826_1118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Issue',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
