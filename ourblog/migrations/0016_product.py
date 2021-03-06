# Generated by Django 4.0.3 on 2022-03-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0015_rename_comm_reply_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('k_price', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
