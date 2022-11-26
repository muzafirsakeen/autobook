# Generated by Django 4.1.2 on 2022-11-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0003_alter_users_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver_detail",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
        migrations.AlterField(
            model_name="driver_detail",
            name="d_email",
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name="driver_detail",
            name="d_fname",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="driver_detail",
            name="d_lname",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="users", name="age", field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name="users", name="phone", field=models.IntegerField(),
        ),
    ]
