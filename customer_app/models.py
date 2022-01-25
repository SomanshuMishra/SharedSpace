from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model

from admin_app.manager import UserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255, null=False, blank=False)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "customer_app"

class CustomerGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255,null=True,blank=True)


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    customer_shipping_address_id = models.CharField(
        max_length=10, null=True, blank=True
    )
    customer_billing_address_id = models.CharField(max_length=10, null=True, blank=True)
    organization_id = models.ForeignKey(Organization,on_delete=models.CASCADE,null=False)
    customer_type = models.ForeignKey(CustomerGroup,on_delete=models.CASCADE)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "customer_app"


class CustomerAddress(models.Model):
    customer_address_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=False, blank=False
    )
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    country_id = models.CharField(max_length=50)
    state_id = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "customer_app"





class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "customer_app"


class State(models.Model):
    id = models.AutoField(primary_key=True)
    state_id = models.CharField(max_length=50)
    state_code = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    country_id = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=False, blank=False
    )
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "customer_app"