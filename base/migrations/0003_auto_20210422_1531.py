# Generated by Django 3.0.5 on 2021-04-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tokenstuff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenstuff',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]