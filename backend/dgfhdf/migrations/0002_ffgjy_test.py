# Generated by Django 2.2.12 on 2020-05-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dgfhdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ffgjy',
            name='test',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
