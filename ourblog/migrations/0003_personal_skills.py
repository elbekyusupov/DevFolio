# Generated by Django 4.0.3 on 2022-03-11 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0002_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ourblog.skill'),
        ),
    ]