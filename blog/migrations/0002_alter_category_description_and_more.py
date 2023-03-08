# Generated by Django 4.1.2 on 2022-12-28 00:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_with_image',
            name='content_after_image',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_with_image',
            name='content_before_image',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post_with_image',
            name='excerpt',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
    ]