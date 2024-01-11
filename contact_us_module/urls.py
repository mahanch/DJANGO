from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsFormView.as_view(), name='contact-us'),
    path('success/', views.success_page, name='success-form-page')
]
