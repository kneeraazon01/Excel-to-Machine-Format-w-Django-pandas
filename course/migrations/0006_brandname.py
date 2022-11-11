# Generated by Django 4.1.2 on 2022-11-01 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0005_alter_store_options_alter_store_market_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BrandName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand_name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Brand Names",
            },
        ),
    ]
