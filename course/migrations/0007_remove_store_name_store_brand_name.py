# Generated by Django 4.1.2 on 2022-11-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0006_brandname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="store",
            name="name",
        ),
        migrations.AddField(
            model_name="store",
            name="brand_name",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="course.brandname",
            ),
        ),
    ]
