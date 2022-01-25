from rest_framework import serializers
# from django.contrib.auth.models import User
from product_app.models import *
from django.conf import settings

class DepartmentSerializer(serializers.ModelSerializer):
	# password = serializers.CharField(required=False, allow_blank=True, allow_null=True, write_only=True)
	class Meta:
		model = Department
		fields = '__all__'
  
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'
        
class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = '__all__'
        
class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductStatus
        fields = '__all__'
        
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'