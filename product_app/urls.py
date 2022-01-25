from django.urls import path, re_path
from django.conf.urls import url

from product_app.views import *
# from service.apis.webhook import webhook_braintree 

urlpatterns = [
	path('product/department', DepartMentView.as_view(), name='admin_register'),
	path('product/attribute', AttributeAddView.as_view(), name='attribute'),
	path('product/attribute_value', AttributeValueView.as_view(), name='attribute'),
	path('product/product_attribute_value', ProductValueApiView.as_view(), name='product_attribute'),
	path('product/product_add', ProductApiView.as_view(), name='product'),
	path('product/product_status', ProductStatusApiView.as_view(), name='product_status'),
	path('product/product_category', ProductCategoryApiView.as_view(), name='product_category'),

	]