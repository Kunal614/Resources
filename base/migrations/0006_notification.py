# Generated by Django 3.0.5 on 2021-04-24 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210422_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
