# Generated by Django 4.1.2 on 2022-11-21 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0009_alter_users_age_alter_users_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver_detail", name="d_phone", field=models.BigIntegerField(),
        ),
    ]
