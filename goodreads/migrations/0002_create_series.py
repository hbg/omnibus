# Generated by Django 2.2.6 on 2019-10-06 20:53

from django.db import migrations, models
import django.db.models.deletion


def create_uncategorized_series(apps, schema_editor):
    # We can't import the Series model directly as it may be a newer version
    # than this migration expects. We use the historical version.
    Series = apps.get_model("goodreads", "Series")

    # Create the Uncategorized series for any Books who do not specify their
    # own series.
    uncategorized = Series(id=0, title="Uncategorized")
    uncategorized.save()


class Migration(migrations.Migration):

    dependencies = [("goodreads", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Series",
            fields=[
                (
                    "id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
            ],
            options={"verbose_name_plural": "Series"},
        ),
        migrations.AddField(
            model_name="book",
            name="series",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="goodreads.Series",
            ),
        ),
        migrations.RunPython(create_uncategorized_series),
    ]