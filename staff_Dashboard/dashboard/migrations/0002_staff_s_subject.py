# Generated by Django 4.2.1 on 2023-06-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="staff",
            name="s_subject",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
