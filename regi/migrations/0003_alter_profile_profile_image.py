# Generated by Django 4.1.2 on 2023-03-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regi', '0002_alter_profile_facebook_alter_profile_github_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
    ]
