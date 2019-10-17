# Generated by Django 2.2.6 on 2019-10-16 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("goodreads", "0003_update_book")]

    operations = [
        migrations.RenameField(
            model_name="book", old_name="published", new_name="publication_day"
        ),
        migrations.RemoveField(model_name="book", name="author"),
        migrations.RemoveField(model_name="book", name="large_image_url"),
        migrations.RemoveField(model_name="book", name="title_without_series"),
        migrations.AddField(
            model_name="author",
            name="average_rating",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="ratings_count",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="author",
            name="role",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="goodreads.Author"),
        ),
        migrations.AddField(
            model_name="book",
            name="isbn",
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publication_month",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publication_year",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="sequence_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="series",
            name="primary_work_count",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="book", name="image_url", field=models.URLField()
        ),
        migrations.AlterField(
            model_name="book",
            name="small_image_url",
            field=models.URLField(null=True),
        ),
    ]