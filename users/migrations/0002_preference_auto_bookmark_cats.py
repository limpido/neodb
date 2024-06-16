# Generated by Django 4.2.13 on 2024-06-16 02:57

from django.db import migrations, models

import users.models.preference


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial_0_10"),
    ]

    operations = [
        migrations.AddField(
            model_name="preference",
            name="auto_bookmark_cats",
            field=models.JSONField(default=users.models.preference._default_book_cats),
        ),
    ]
