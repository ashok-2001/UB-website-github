# Generated by Django 4.1.2 on 2023-02-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_remove_post_likes_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
