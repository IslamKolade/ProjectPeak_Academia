# Generated by Django 4.2 on 2023-07-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectPeak_Academia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("facebook_url", models.URLField(blank=True, null=True)),
                (
                    "instagram_username",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                (
                    "twitter_username",
                    models.CharField(blank=True, max_length=300, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=200)),
                ("email", models.CharField(blank=True, max_length=200)),
                ("whatsapp_number", models.CharField(blank=True, max_length=100)),
                ("phone_number", models.CharField(blank=True, max_length=100)),
                ("about", models.CharField(blank=True, max_length=10000)),
                ("description", models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.AlterField(
            model_name="course",
            name="projects_count",
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name="course",
            name="url",
            field=models.SlugField(
                blank=True, editable=False, max_length=100, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="url",
            field=models.SlugField(
                blank=True, editable=False, max_length=100, unique=True
            ),
        ),
    ]
