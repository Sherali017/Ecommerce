from django.contrib import admin

from products.forms import ColorModelForm
from products.models import CategoryModel, BrandModel, ProductTagModel, ProductModel, SizeModel, ColorModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(ProductModel)
class PrdouctModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'created_at']
    list_filter = ['created_at', 'price']
    readonly_fields = ['real_price']
    search_fields = ['title', 'price', 'created_at']


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code' ]
    list_filter = ['created_at']
    search_fields = ['code' ]
    form = ColorModelForm

