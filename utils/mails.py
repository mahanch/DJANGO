from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.conf import settings


def send_email(subject, to, template, context):
    try:
        html_message = render_to_string(template, context)
        optimize_message = strip_tags(html_message)
        source_email = settings.EMAIL_HOST_USER
        send_mail(subject, optimize_message, source_email, [to], html_message=html_message)

    except:
        pass
