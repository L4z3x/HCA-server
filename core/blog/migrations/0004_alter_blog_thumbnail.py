# Generated by Django 5.1.6 on 2025-04-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_comment_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="blog-thumbnails/"
            ),
        ),
    ]
