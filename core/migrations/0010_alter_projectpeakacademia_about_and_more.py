# Generated by Django 4.2.4 on 2023-08-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_our_services"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="account_name",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="account_number",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="bank_name",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="email",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="phone_number",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name="projectpeakacademia",
            name="whatsapp_number",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
