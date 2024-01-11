from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from user_module.forms import RegisterForm, LoginForm, ForgotPassForm, ResetPasswordForm
from utils.mails import send_email

from .models import User


# Create your views here.

class LoginView(View):

    def get(self, request):
        context = {
            'LoginForm': LoginForm

        }
        return render(request, 'user_module/login_page.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'نام کاربری شما تایید نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('password', 'پسورد وارد شده درست نمیباشد')
            else:
                login_form.add_error('email', 'ایمیل درست نمیباشد')

        context = {
            'LoginForm': login_form

        }
        return render(request, 'user_module/login_page.html', context)


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'registerform': register_form

        }
        return render(request, 'user_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=email).exists()
            if user:
                register_form.add_error('email', 'این ایمیل قبلا ذخیره شده است')
            else:
                new_user = User(
                    email=email,
                    is_active=False,
                    email_active_code=get_random_string(72),
                    username=email
                )
                new_user.set_password(password)
                new_user.save()

                send_email('ثبت نام کاربر', new_user.email, 'emails/register_activation.html',
                           {'user': new_user})
                return redirect(reverse('login_page'))
        context = {
            'registerform': register_form

        }
        return render(request, 'user_module/register_page.html', context)


class ActivateCodeView(View):
    def get(self, request, activation_code):
        user: User = User.objects.filter(email_active_code__iexact=activation_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            # todo:show account activated message
            else:
                # todo:show account was activated before
                pass
        else:
            raise Http404


class ForgotpasswordView(View):
    def get(self, request: HttpRequest):
        forget_password_form = ForgotPassForm()
        context = {
            'forget_pass_form': forget_password_form
        }
        return render(request, 'user_module/forget_pass.html', context)

    def post(self, request: HttpRequest):
        forget_password_form = ForgotPassForm(request.POST)
        user_email = forget_password_form.cleaned_data.get('email')
        if forget_password_form.is_valid():
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is None:
                redirect(reverse('login_page'))
            else:
                send_email('فعال سازی حساب کاربری', user.email, 'emails/forget_active_account.html',
                           {'user': user})
                return redirect(reverse('login_page'))

        context = {
            'forget_pass_form': forget_password_form
        }
        return render(request, 'user_module/forget_pass.html', context)


class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm()
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user == None:
            return redirect(reverse('login_page'))

        context = {
            'reset_pass_from': reset_pass_form
        }
        return render(request, 'user_module/reset_password_page.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is not None:
                user_password = reset_pass_form.cleaned_data.get('password')
                user.set_password(user_password)
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))
            else:
                raise Http404
        else:
            return redirect(reverse('home_page'))

def logut_view(request):
    logout(request)
    return redirect(reverse('login_page'))

