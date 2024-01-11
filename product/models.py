from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='دسته بندی', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='دسته بندی در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name="برند")
    is_active = models.BooleanField(verbose_name="فعال/غیر فعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"


class Products(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    category = models.ManyToManyField(ProductCategory, verbose_name='دسته بندی')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    short_description = models.CharField(max_length=600, default="there is no data here", verbose_name='توضیحات کوتاه',
                                         db_index=True)
    description = models.TextField(verbose_name='توضیحات', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    slug = models.SlugField(default="", null=False, unique=True, max_length=300, allow_unicode=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='تگ محصول', db_index=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصول'

# Create your models here.
