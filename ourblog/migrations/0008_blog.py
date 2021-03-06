# Generated by Django 4.0.3 on 2022-03-11 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0007_personal_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]
