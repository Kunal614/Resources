# Generated by Django 3.0.7 on 2021-04-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0004_cp_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField(blank=True, null=True)),
                ('session', models.URLField(blank=True, max_length=300, null=True)),
                ('resource', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
