# Generated by Django 4.1.4 on 2022-12-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("name", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="pics")),
                ("desc1", models.TextField()),
                ("desc2", models.TextField()),
            ],
        ),
    ]
