# Generated by Django 4.0.4 on 2022-06-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_product_image2_product_image3_product_image4'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
