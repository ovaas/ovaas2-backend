# Generated by Django 3.2 on 2021-11-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=128)),
                ('app_name_en', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('description_en', models.TextField()),
                ('thumbnail_url', models.CharField(max_length=128)),
                ('page_url', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DeployStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=50)),
            ],
        ),
    ]
