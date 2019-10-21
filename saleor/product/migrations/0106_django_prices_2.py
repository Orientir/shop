# Generated by Django 2.2.4 on 2019-08-14 09:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0105_product_minimal_variant_price")]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="price", new_name="price_amount"
        ),
        migrations.RenameField(
            model_name="productvariant",
            old_name="cost_price",
            new_name="cost_price_amount",
        ),
        migrations.RenameField(
            model_name="productvariant",
            old_name="price_override",
            new_name="price_override_amount",
        ),
        migrations.AddField(
            model_name="product",
            name="currency",
            field=models.CharField(
                default=settings.DEFAULT_CURRENCY,
                max_length=settings.DEFAULT_CURRENCY_CODE_LENGTH,
            ),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="currency",
            field=models.CharField(
                blank=True,
                default=settings.DEFAULT_CURRENCY,
                max_length=settings.DEFAULT_CURRENCY_CODE_LENGTH,
                null=True,
            ),
        ),
    ]
