# Generated by Django 4.2.3 on 2023-10-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="image",
            field=models.ImageField(default=None, upload_to="img/"),
        ),
    ]