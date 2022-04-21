# Generated by Django 4.0.3 on 2022-03-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0003_personal_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='skills',
        ),
        migrations.AddField(
            model_name='personal',
            name='skills',
            field=models.ManyToManyField(to='ourblog.skill'),
        ),
    ]
