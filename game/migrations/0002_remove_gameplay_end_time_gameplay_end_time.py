# Generated by Django 4.1.7 on 2023-03-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameplay',
            name='End_time',
        ),
        migrations.AddField(
            model_name='gameplay',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
