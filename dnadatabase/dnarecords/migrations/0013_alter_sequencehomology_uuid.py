# Generated by Django 4.1.1 on 2022-11-07 05:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("dnarecords", "0012_alter_sequencehomology_uuid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sequencehomology",
            name="uuid",
            field=models.UUIDField(
                default=uuid.UUID("5642e83d-c232-4385-b898-9c4082ad25ce")
            ),
        ),
    ]
