from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()


@register.filter(name="jalali_date")
def jalali_date(value):
    return date2jalali(value).strftime('%y/%m/%d')


@register.filter(name="jalali_time")
def jalali_time(value):
    return datetime2jalali(value).strftime('%H:%M')
