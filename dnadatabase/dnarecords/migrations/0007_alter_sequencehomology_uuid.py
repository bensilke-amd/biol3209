# Generated by Django 4.1 on 2022-09-13 00:23

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dnarecords", "0006_alter_sequencehomology_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sequencehomology",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("5f1c3f5b-6fa9-4296-96ae-a68676433226")
            ),
        ),
    ]
