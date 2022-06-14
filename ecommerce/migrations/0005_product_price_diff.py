# Generated by Django 4.0.4 on 2022-06-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_cart_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_diff',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]