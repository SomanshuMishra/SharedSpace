from django.urls import path, re_path
from django.conf.urls import url

from admin_app.views import *
# from service.apis.webhook import webhook_braintree 

urlpatterns = [
	url('administratior/register', AdminRegisterApiView.as_view(), name='admin_register'),
	url('administratior/login', AdminLoginApiView.as_view(), name='admin_login'),
	url('administratior/logout', LogoutApiView.as_view(), name='admin_login'),
	url('administratior/forgot_password', ForgotPasswordLinkView.as_view(), name='admin_login'),
	url('administratior/change_password', ChangePasswordView.as_view(), name='admin_login'),

	]