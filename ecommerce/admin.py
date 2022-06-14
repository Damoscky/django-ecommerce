from .models import Cart
from .models import Product
from .models import Category
from .models import SubCategory
from .models import ChildCategory

from django.contrib import admin

admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(ChildCategory)