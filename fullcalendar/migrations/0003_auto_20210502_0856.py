# Generated by Django 2.2.20 on 2021-05-02 08:56

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        ('fullcalendar', '0002_publicevent_community'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', colorful.fields.RGBColorField(null=True)),
                ('community', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community.Community')),
            ],
        ),
        migrations.AddField(
            model_name='publicevent',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fullcalendar.Category'),
        ),
    ]
