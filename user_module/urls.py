from django.urls import path
from user_module import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register_page'),
    path('login', views.LoginView.as_view(), name='login_page'),
    path('forget-password', views.ForgotpasswordView.as_view(), name='forgot-pass-page'),
    path('reset-password/<active_code>', views.ResetPassword.as_view(), name='reset-pass-page'),
    path('logout', views.logut_view, name='logout_page'),
    path('active-code/<activation_code>', views.ActivateCodeView.as_view(), name='activation_page'),
]
