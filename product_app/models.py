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
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_code = models.CharField(max_length=150, null=True, blank=True)
    dept_name = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class ProductStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, null=True, blank=True)
    parent_category_id = models.CharField(max_length=50, null=True, blank=True)
    category_level = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    nr_items = models.CharField(max_length=50, null=True, blank=True)
    temprelationship = models.CharField(max_length=50, null=True, blank=True)
    dept_code = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    dept_name = models.CharField(max_length=50, null=True, blank=True)
    key = models.CharField(max_length=50, null=True, blank=True)
    nefault_group_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150)
    product_short_description = models.TextField(null=True, blank=True)
    product_long_description = models.TextField(null=True, blank=True)
    product_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    product_status = models.ForeignKey(
        ProductStatus, on_delete=models.CASCADE, null=False
    )
    product_retail_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    product_wholesale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    product_dealer_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    product_tax = models.CharField(max_length=50, null=True, blank=True)
    product_category_id = models.ForeignKey(
        Categories, on_delete=models.CASCADE, null=False
    )
    group_id = models.CharField(max_length=50, null=True, blank=True)
    product_notes = models.TextField(null=True, blank=True)
    product_info = models.TextField(null=True, blank=True)
    product_weight = models.CharField(max_length=50, null=True, blank=True)
    product_unite = models.CharField(max_length=50, null=True, blank=True)
    product_qty_hold = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    product_order_limit = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class ProductImages(models.Model):
    images_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    image_url = models.CharField(max_length=500, null=True, blank=True)
    image_name = models.CharField(max_length=50, null=True, blank=True)
    image_caption = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=50, null=True, blank=True)
    attribute_type = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class AttributeValue(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_id = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=False)
    attribute_value = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class ProductAttribute(models.Model):
    product_attribute_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    prodict_attribute_value_id = models.ForeignKey(
        AttributeValue, on_delete=models.CASCADE, null=False
    )

    class Meta:
        app_label = "product_app"


class OrderProductAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    product_attribute_id = models.ForeignKey(
        ProductAttribute, on_delete=models.CASCADE, null=False
    )
    order_product_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"


class Product_Location(models.Model):
    product_location_id = models.CharField(max_length=50, null=True, blank=True)
    product_id = models.CharField(max_length=50, null=True, blank=True)
    location_id = models.CharField(max_length=50, null=True, blank=True)
    product_quantity = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = "product_app"
