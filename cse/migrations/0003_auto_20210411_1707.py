# Generated by Django 3.0.7 on 2021-04-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0002_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='cp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('data', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='person',
        ),
    ]
