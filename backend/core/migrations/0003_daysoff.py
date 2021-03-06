# Generated by Django 2.2 on 2020-11-08 02:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_team_slug_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOff',
            fields=[
                ('created', models.DateTimeField(default=datetime.datetime.now, help_text='Cuando el objeto fue creado', verbose_name='created at')),
                ('modified', models.DateTimeField(default=datetime.datetime.now, help_text='Cuando fue modificado por ultima vez', verbose_name='modified at')),
                ('day', models.DateField(primary_key=True, serialize=False)),
                ('requested', models.BooleanField(default=False)),
                ('note', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'day')},
            },
        ),
    ]
