# Generated by Django 5.1.4 on 2025-01-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator_app', '0004_product_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldata',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
