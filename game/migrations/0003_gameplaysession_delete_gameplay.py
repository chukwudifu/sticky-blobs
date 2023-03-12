# Generated by Django 4.1.7 on 2023-03-12 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_remove_gameplay_end_time_gameplay_end_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='GamePlaySession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('total_game_time', models.CharField(blank=True, max_length=50, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_time_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='GamePlay',
        ),
    ]
