# Generated by Django 5.1.6 on 2025-03-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_budget_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
