# Generated by Django 4.0.4 on 2022-06-13 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_product_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
