# Generated by Django 4.2.4 on 2023-08-31 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_projectpeakacademia_account_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project_request",
            name="phone_number",
            field=models.IntegerField(blank=True, max_length=10000, null=True),
        ),
    ]