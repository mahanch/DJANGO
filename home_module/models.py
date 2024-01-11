from django.db import models


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/slider', verbose_name='تصویر')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_name = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = "اسلایدر ها"

    def __str__(self):
        return self.title
