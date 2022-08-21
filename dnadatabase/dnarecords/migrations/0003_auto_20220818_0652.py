# Generated by Django 3.2.6 on 2022-08-18 06:52

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dnarecords", "0002_auto_20220818_0622"),
    ]

    operations = [
        migrations.CreateModel(
            name="Environment",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                (
                    "description",
                    models.TextField(
                        help_text="A description of the environment or type of environment.",
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Taxonomy",
            fields=[
                ("uuid", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, null=True)),
                (
                    "description",
                    models.TextField(
                        help_text="A description of the taxonomy. More information if no url can be provided.",
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="databasereference",
            name="feature",
        ),
        migrations.RemoveField(
            model_name="sequence",
            name="relations",
        ),
        migrations.AddField(
            model_name="sequence",
            name="locus",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="sequence",
            name="other",
            field=models.JSONField(
                help_text="Other information about the sequence. Information which does not fit into the above categories.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="sequence",
            name="version",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="database",
            name="description",
            field=models.TextField(
                help_text="A description of the database. More information if no url can be provided.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="sequence",
            name="sequence",
            field=models.TextField(help_text="The nt's of the sequence", null=True),
        ),
        migrations.CreateModel(
            name="DatabaseSequenceReference",
            fields=[
                (
                    "databasereference_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dnarecords.databasereference",
                    ),
                ),
                (
                    "sequence",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dnarecords.sequence",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("dnarecords.databasereference",),
        ),
        migrations.AddField(
            model_name="sequence",
            name="environment",
            field=models.ManyToManyField(to="dnarecords.Environment"),
        ),
        migrations.AddField(
            model_name="sequence",
            name="taxonomy",
            field=models.ManyToManyField(to="dnarecords.Taxonomy"),
        ),
        migrations.CreateModel(
            name="DatabaseFeatureReference",
            fields=[
                (
                    "databasereference_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="dnarecords.databasereference",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dnarecords.feature",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("dnarecords.databasereference",),
        ),
    ]