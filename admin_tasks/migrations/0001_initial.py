# Generated by Django 5.1.2 on 2024-11-11 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unnamed Shape', help_text='Name or identifier for the shape', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Detailed description of the shape')),
                ('shape_data', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_sold', models.BooleanField(default=False)),
                ('facing', models.CharField(default='north', max_length=100)),
                ('size', models.CharField(choices=[('SMALL', 'Up to 15 cents'), ('MEDIUM', '15-30 cents'), ('LARGE', 'Above 30 cents')], default='SMALL', max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shapes', to='admin_tasks.category')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files_app.file')),
            ],
        ),
    ]
