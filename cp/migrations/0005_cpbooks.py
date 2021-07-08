# Generated by Django 3.2.5 on 2021-07-08 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0004_auto_20210419_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(default='NA', max_length=200)),
                ('view_down', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
