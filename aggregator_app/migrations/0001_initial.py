# Generated by Django 5.1.4 on 2025-01-14 16:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_link', models.URLField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.CharField(max_length=50)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('number_of_ratings', models.CharField(max_length=50)),
                ('specifications', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_link', models.URLField(max_length=500)),
                ('image_url', models.URLField(max_length=500)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.CharField(max_length=50)),
                ('rating', models.CharField(blank=True, max_length=10, null=True)),
                ('number_of_ratings', models.CharField(blank=True, max_length=50, null=True)),
                ('specifications', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
