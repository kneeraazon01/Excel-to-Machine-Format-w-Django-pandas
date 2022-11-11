# Generated by Django 4.1.2 on 2022-10-31 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="market_id",
            field=models.ForeignKey(
                blank=True,
                default=111111,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="market",
                to="course.marketid",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="store_number",
            field=models.ForeignKey(
                blank=True,
                default=1111,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="store",
                to="course.storenumber",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="terminal_id",
            field=models.ForeignKey(
                blank=True,
                default=111,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="terminal",
                to="course.terminalid",
            ),
        ),
    ]
