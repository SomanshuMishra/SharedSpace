from django.db import models
from django.conf import settings

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model

from admin_app.manager import UserManager

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# from customer_app.models import Customer
# from poduct_app.models import Customer

# Create your models here.


class Orders(models.Model):
	order_id = models.AutoField(primary_key=True)
	customer_id = models.CharField(max_length=50, null=True , blank=True)
	order_created_date = models.DateTimeField(auto_now_add=True)
	order_qty = models.CharField(max_length=50, null=True , blank=True)
	order_price = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
	order_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
	order_status = models.CharField(max_length=50, null=True , blank=True)
	order_updated_date = models.DateTimeField(auto_now=True)
	order_special_instruction = models.TextField(null=True , blank=True)
	order_packed_by = models.CharField(max_length=50, null=True , blank=True)
	order_packed_time = models.DateTimeField(auto_now_add=True)
	customer_billing_id = models.CharField(max_length=50, null=True , blank=True)
	createad_at = models.DateTimeField(auto_now_add=True)
	class Meta:
		app_label = 'order_app'

class OrderStatus(models.Model):
	order_status_id = models.AutoField(primary_key=True)
	order_status_name = models.CharField(max_length=50, null=True , blank=True)
	class Meta:
		app_label = 'order_app' 


class WareHouse(models.Model):
	warehouse_id = models.AutoField(primary_key=True)
	warehouse_name = models.CharField(max_length=50, null=True , blank=True)
	warehouse_position = models.CharField(max_length=50, null=True , blank=True)
	warehouse_status = models.CharField(max_length=50, null=True , blank=True)
	class Meta:
		app_label = 'order_app'
class WareHouseLocation(models.Model):
	location_id = models.AutoField(primary_key=True)
	warehouse_id = models.ForeignKey(WareHouse,on_delete=models.CASCADE,null=False,blank=False)
	location_name = models.CharField(max_length=50, null=True , blank=True)
	class Meta:
		app_label = 'order_app'

class OrderProducts(models.Model):
	id  = models.AutoField(primary_key=True)
	order_id = models.ForeignKey(Orders,on_delete=models.CASCADE,null=False,blank=False)
	order_product_id = models.CharField(max_length=50, null=True , blank=True)
	order_product_qty = models.CharField(max_length=50, null=True , blank=True)
	order_product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
	order_product_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
	order_product_location_id = models.CharField(max_length=50, null=True , blank=True)
	order_product_status_id = models.ForeignKey(OrderStatus,on_delete=models.CASCADE,null=False,blank=False)
	order_product_warehouse_position = models.ForeignKey(WareHouseLocation,on_delete=models.CASCADE,null=False,blank=False)
	class Meta:
		app_label = 'order_app'
	

class OrderTracking(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_product_id = models.CharField(max_length=50, null=True , blank=True)
	order_tracking_id = models.CharField(max_length=50, null=True , blank=True)
	order_delivery_date = models.CharField(max_length=50, null=True , blank=True)
	order_shipping_id = models.CharField(max_length=50, null=True , blank=True)
	order_tracking_info = models.CharField(max_length=50, null=True , blank=True)
	class Meta:
		app_label = 'order_app'

class ShippingInfo(models.Model):
	shipping_id = models.AutoField(primary_key=True)
	shipping_name = models.CharField(max_length=50, null=True , blank=True)
	shipping_type = models.CharField(max_length=50, null=True , blank=True)
	shipping_price = models.DecimalField(max_digits=10, decimal_places=2, null=True , blank=True)
	class Meta:
		app_label = 'order_app'



