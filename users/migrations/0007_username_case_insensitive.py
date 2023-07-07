# Generated by Django 4.2.3 on 2023-07-07 00:16

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_unique_email"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="unique_mastodon_username",
        ),
        migrations.RemoveConstraint(
            model_name="user",
            name="unique_mastodon_id",
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("email"), name="unique_email"
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("username"),
                name="unique_username",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("mastodon_username"),
                django.db.models.functions.text.Lower("mastodon_site"),
                name="unique_mastodon_username",
            ),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("mastodon_id"),
                django.db.models.functions.text.Lower("mastodon_site"),
                name="unique_mastodon_id",
            ),
        ),
    ]