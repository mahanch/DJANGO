from django.db import models


# Create your models here.
class Contact_us(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    full_name = models.CharField(max_length=300, verbose_name='نام کامل')
    email = models.EmailField(max_length=500, verbose_name='ایمیل')
    message = models.TextField(verbose_name='توضیحات')
    is_read = models.BooleanField(verbose_name='خوانده شده',default=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='پاسخ ادمین', null=True, blank=True)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
