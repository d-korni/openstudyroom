# Generated by Django 2.2.10 on 2020-06-07 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20, unique=True)),
                ('username', models.CharField(max_length=254)),
                ('discriminator', models.CharField(max_length=4)),
                ('avatar', models.CharField(blank=True, max_length=32)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('access_token', models.CharField(blank=True, max_length=32)),
                ('refresh_token', models.CharField(blank=True, max_length=32)),
                ('scope', models.CharField(blank=True, max_length=256)),
                ('expiry', models.DateTimeField(null=True)),
                ('status', models.CharField(blank=True, max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discord_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiscordInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('description', models.CharField(blank=True, max_length=256)),
                ('guild_name', models.CharField(blank=True, max_length=64)),
                ('guild_id', models.CharField(blank=True, max_length=20)),
                ('guild_icon', models.CharField(blank=True, max_length=32)),
                ('channel_name', models.CharField(blank=True, max_length=64)),
                ('channel_id', models.CharField(blank=True, max_length=20)),
                ('channel_type', models.CharField(blank=True, choices=[('text', 'text'), ('voice', 'voice')], max_length=5)),
                ('groups', models.ManyToManyField(blank=True, related_name='discord_invites', to='auth.Group')),
            ],
        ),
    ]
