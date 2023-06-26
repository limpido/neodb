# Generated by Django 3.2.19 on 2023-06-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0004_alter_localactivity_template"),
    ]

    operations = [
        migrations.AlterField(
            model_name="localactivity",
            name="template",
            field=models.CharField(
                choices=[
                    ("mark_item", "Markitem"),
                    ("review_item", "Reviewitem"),
                    ("create_collection", "Createcollection"),
                    ("like_collection", "Likecollection"),
                    ("feature_collection", "Featurecollection"),
                    ("comment_child_item", "Commentchilditem"),
                    ("comment_focus_item", "Commentfocusitem"),
                ],
                max_length=50,
            ),
        ),
    ]