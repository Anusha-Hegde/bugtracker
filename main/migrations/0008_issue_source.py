# Generated by Django 3.1 on 2020-08-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200831_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='source',
            field=models.CharField(default='', max_length=250),
        ),
    ]
