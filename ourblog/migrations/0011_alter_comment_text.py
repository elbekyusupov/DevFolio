# Generated by Django 4.0.3 on 2022-03-12 11:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ourblog', '0010_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]