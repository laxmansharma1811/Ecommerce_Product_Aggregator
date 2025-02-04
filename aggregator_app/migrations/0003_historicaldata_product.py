# Generated by Django 5.1.4 on 2025-01-17 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator_app', '0002_historicaldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldata',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='aggregator_app.product'),
        ),
    ]
