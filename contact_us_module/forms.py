from .models import Contact_us
from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمیتواند بیشتر از 50 کاراکتر باشد'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کامل'
        }))
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }))
    subject = forms.CharField(
        label='عنوان',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }))
    text = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                "id": 'message',
                'placeholder': 'متن پیام'
            }))


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['title', 'email', 'full_name', 'message']
        widgets = {
            "full_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام کامل شما'
            }),

            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان'
            }),
            "email": forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ایمیل'
            }),
            "message": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'id': 'message'
            }),

        }
