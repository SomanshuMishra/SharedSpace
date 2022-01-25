from django.urls import path, re_path
from django.conf.urls import url

from admin_app.views import *
# from service.apis.webhook import webhook_braintree 

urlpatterns = [
	path('administratior/register', AdminRegisterApiView.as_view(), name='admin_register'),
	path('administratior/login', AdminLoginApiView.as_view(), name='admin_login'),
	path('administratior/logout', LogoutApiView.as_view(), name='admin_logout'),
	path('administratior/forgot_password', ForgotPasswordLinkView.as_view(), name='forgot_password'),
	path('administratior/change_password', ChangePasswordView.as_view(), name='change_password'),
	path('administratior/admin_crud', AdiminCrudApiView.as_view(), name='admin_crud'),
	path('administratior/role', RolesApiView.as_view(), name='admin_role'),
	path('administratior/role_resource', RoleResourcesApiView.as_view(), name='admin_role_resource'),
	path('administratior/resource_delete', RoleResourcesDelApiView.as_view(), name='admin_role_resource'),
	path('administratior/admin_list', AdminListApiView.as_view(), name='admin_list'),


	]