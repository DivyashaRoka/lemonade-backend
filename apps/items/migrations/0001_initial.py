# Generated by Django 3.2.1 on 2021-11-09 14:57

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_index=True, default='inactive', max_length=15, verbose_name='status')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=14, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='price')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
