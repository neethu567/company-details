# Generated by Django 3.1.1 on 2021-03-12 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("companyapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="address_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="companyapp.company",
            ),
        ),
    ]
