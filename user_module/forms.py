from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        validators=[validators.EmailValidator],
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),

    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار رمز عبور'
        }),

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirmpas = self.cleaned_data.get('confirm_password')
        if confirmpas == password:
            return confirmpas
        raise ValidationError('رمز عبور با تکرار رمز عبور مغایرت دارد')


class LoginForm(forms.Form):
    email = forms.EmailField(

        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),

    )


class ForgotPassForm(forms.Form):
    email = forms.EmailField(

        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder': 'ایمیل'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور'
        }),

    )

    confirm_password = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار رمز عبور'
        }),

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirmpas = self.cleaned_data.get('confirm_password')
        if confirmpas == password:
            return confirmpas
        raise ValidationError('رمز عبور با تکرار رمز عبور مغایرت دارد')
