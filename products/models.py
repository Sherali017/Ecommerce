from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

UserModel = get_user_model()

class CategoryModel(models.Model):
    title= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class BrandModel(models.Model):
    title= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

class ProductTagModel(models.Model):
    title=  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product tag'
        verbose_name_plural = 'product tags'

class SizeModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'size'
        verbose_name_plural  ='sizes'

class ColorModel(models.Model):
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField()


    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'



class ProductModel(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    size = models.ManyToManyField(SizeModel, related_name='products')
    color = models.ManyToManyField(ColorModel, related_name='products')
    wishlist = models.ManyToManyField(UserModel, related_name='wishlist', )
    discount = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    short_description = models.TextField()
    long_description = RichTextUploadingField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    @staticmethod
    def get_from_cart( request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(pk__in=cart)







    def is_discount(self):
        return self.price != 0



    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/tashkent')) - self.created_at
        return diff.days <= 3

    def get_related_products(self):
        return self.category.products.exclude(pk=self.pk)



    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'




