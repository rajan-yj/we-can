# Generated by Django 4.0.1 on 2022-01-27 17:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('can', '0002_can_can_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='can',
            old_name='filled',
            new_name='reported',
        ),
        migrations.AlterField(
            model_name='can',
            name='can_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
