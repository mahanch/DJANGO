from django.contrib import admin
from site_module import models

# Register your models here.


admin.site.register(models.SiteSettings)
admin.site.register(models.FooterlinkTitle)
admin.site.register(models.FooterLink)
