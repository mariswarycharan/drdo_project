# Generated by Django 4.2.4 on 2023-08-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Upload_XTF_File_model",
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
                ("xtf_file", models.FileField(upload_to="media/")),
            ],
        ),
    ]