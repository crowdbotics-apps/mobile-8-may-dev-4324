# Generated by Django 2.2.12 on 2020-05-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20200508_1205"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="nnbn",
            field=models.ManyToManyField(
                blank=True, related_name="user_nnbn", to="home.HomePage"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
