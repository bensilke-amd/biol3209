# Generated by Django 4.1 on 2022-09-13 00:22

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dnarecords", "0005_alter_sequencehomology_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sequencehomology",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("3540e99b-8b0a-44f8-86f5-7f8c3db13a1f")
            ),
        ),
    ]
