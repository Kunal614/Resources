# Generated by Django 3.2.5 on 2021-07-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DevBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='NA', max_length=200)),
                ('view_down', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
