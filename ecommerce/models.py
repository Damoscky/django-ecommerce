from datetime import datetime
from tkinter import CASCADE
from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class ChildCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=3000)
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    new_price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True, blank=True)
    childcategory = models.ForeignKey('ChildCategory', on_delete=models.CASCADE, null=True, blank=True)
    price_diff = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    image = models.TextField(max_length=3000)
    image2 = models.TextField(max_length=3000, null=True, blank=True)
    image3 = models.TextField(max_length=3000, null=True, blank=True)
    image4 = models.TextField(max_length=3000, null=True, blank=True)
    quantity = models.IntegerField()
    quantity_purchased = models.IntegerField(default=0)
    sku = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.new_price}'
        

class Cart(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user_id














