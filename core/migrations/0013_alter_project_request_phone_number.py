# Generated by Django 4.2.4 on 2023-08-31 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_project_request_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project_request",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
