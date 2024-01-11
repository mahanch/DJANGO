from django.db import models


# Create your models here.

class SiteSettings(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم')
    site_url = models.CharField(max_length=200, verbose_name='url سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, verbose_name='شماره تماس', null=True, blank=True)
    fax = models.CharField(max_length=200, verbose_name='فکس', null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us = models.TextField(verbose_name='درباره سایت')
    site_logo = models.ImageField(upload_to='images/sitelogo', verbose_name='لوگو سایت')
    is_main_settings = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.name


class FooterlinkTitle(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterlinkTitle, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = ' لینک های فوتر'
        verbose_name_plural = 'لینک فوتر'

    def __str__(self):
        return self.title

