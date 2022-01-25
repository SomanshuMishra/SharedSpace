from rest_framework import serializers
# from django.contrib.auth.models import User
from admin_app.models import *
from django.conf import settings

class AdminSerializer(serializers.ModelSerializer):
	password = serializers.CharField(required=False, allow_blank=True, allow_null=True, write_only=True)
	class Meta:
		model = Admins
		fields = '__all__'

class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Roles
		fields = '__all__'

class RoleResourcesSerializer(serializers.ModelSerializer):
	class Meta:
		model = RoleResources
		fields = '__all__'