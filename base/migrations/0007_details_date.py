# Generated by Django 3.0.5 on 2021-04-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
