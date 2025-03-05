# Generated by Django 5.1.6 on 2025-03-05 07:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_budget'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='budget', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
