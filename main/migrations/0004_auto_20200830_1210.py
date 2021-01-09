# Generated by Django 3.1 on 2020-08-30 12:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20200830_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='category',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='is_open',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='user',
        ),
        migrations.AddField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='closed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='issue',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='opened',
            field=models.DateField(default=datetime.date(2020, 8, 30)),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('in progress', 'in progress'), ('resolved', 'resolved'), ('closed', 'closed'), ('duplicate', 'duplicate')], default='open', max_length=30),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('critical', 'critical'), ('high', 'high'), ('normal', 'normal'), ('low', 'low')], default='low', max_length=30),
        ),
    ]