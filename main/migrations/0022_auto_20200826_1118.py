# Generated by Django 3.1 on 2020-08-26 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200826_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='proj_id',
            field=models.ForeignKey(db_column='Project.id', on_delete=django.db.models.deletion.CASCADE, to='main.project'),
        ),
    ]
