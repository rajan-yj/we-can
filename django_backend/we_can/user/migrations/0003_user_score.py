# Generated by Django 4.0.1 on 2022-01-30 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
