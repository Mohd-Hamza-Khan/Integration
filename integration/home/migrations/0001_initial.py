# Generated by Django 4.2.4 on 2024-01-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("taskTitle", models.CharField(max_length=30)),
                ("taskDes", models.TextField()),
                ("time", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
