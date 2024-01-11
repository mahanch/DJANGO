from django.contrib import admin
from . import models

admin.site.register(models.Products)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductTag)
admin.site.register(models.ProductBrand)

# Register your models here.


from . import models
