# Generated by Django 2.2.6 on 2019-10-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("goodreads", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="book",
            name="rating",
            field=models.IntegerField(null=True),
        )
    ]
