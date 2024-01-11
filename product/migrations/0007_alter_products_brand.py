# Generated by Django 5.0 on 2023-12-24 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productbrand', verbose_name='برند'),
        ),
    ]
