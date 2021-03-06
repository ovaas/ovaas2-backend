# Generated by Django 3.2.9 on 2021-12-05 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=128)),
                ('name_en', models.CharField(max_length=128)),
                ('description_ja', models.TextField()),
                ('description_en', models.TextField()),
                ('endpoint_url', models.CharField(max_length=128)),
                ('thumbnail_uri', models.CharField(max_length=128)),
                ('gui_type', models.CharField(choices=[('image_upload', 'Image Upload'), ('draw', 'Draw')], max_length=128)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
