# Generated by Django 3.2.16 on 2023-02-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mastodon", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mastodonapplication",
            name="api_domain",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="domain for api call"
            ),
        ),
        migrations.AddField(
            model_name="mastodonapplication",
            name="server_version",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="type and verion"
            ),
        ),
    ]
