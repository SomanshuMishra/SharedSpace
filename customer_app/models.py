from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True , blank=True)
    last_name = models.CharField(max_length=50, null=True , blank=True)
    email_address = models.CharField(max_length=50, null=True , blank=True)
    phone_number = models.CharField(max_length=15, null=True , blank=True)
    zip = models.CharField(max_length=10, null=True , blank=True)
    customer_shipping_address_id = models.CharField(max_length=10, null=True , blank=True)
    customer_billing_address_id = models.CharField(max_length=10, null=True , blank=True)
    organization_id = models.CharField(max_length=10, null=True , blank=True)
    customer_type = models.CharField(max_length=10, null=True , blank=True)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'customer_app'
    
    
class CustomerAddress(models.Model):
    customer_address_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE,null=False,blank=False)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    country_id =  models.CharField(max_length=50)
    state_id =  models.CharField(max_length=50)
    zip =  models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'customer_app'

class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255,null=False,blank=False)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'customer_app'

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'customer_app'
    
    
class State(models.Model):
    id = models.AutoField(primary_key=True)
    state_id = models.CharField(max_length=50)
    state_code = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    country_id = models.ForeignKey(Country,on_delete=models.CASCADE,null=False,blank=False)
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        app_label = 'customer_app'
    

