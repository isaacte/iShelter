# Generated by Django 5.0.3 on 2024-03-16 10:12

import shelter.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelter', '0002_alter_catbreed_name_alter_dogbreed_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='main',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]