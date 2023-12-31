# Generated by Django 4.2.3 on 2023-10-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0004_alter_curso_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="instrutor",
            name="foto",
            field=models.ImageField(default=None, upload_to="img/instructors_pics/"),
        ),
        migrations.AlterField(
            model_name="curso",
            name="image",
            field=models.ImageField(upload_to="img/courses_pics/"),
        ),
    ]
