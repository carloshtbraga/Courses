# Generated by Django 4.2.3 on 2023-10-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0005_instrutor_foto_alter_curso_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="curso",
            name="data_envio",
            field=models.DateTimeField(auto_now=True),
        ),
    ]