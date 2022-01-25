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

# from django.utils.translation import ugettext_lazy as _


class Roles(models.Model):
	role_name = models.CharField(max_length=50, null=True, blank=True)
	role_code = models.CharField(max_length=50, null=True, blank=True)
	role_status = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		app_label = 'admin_app'



class RoleResources(models.Model):
	role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False, blank=False)
	resource_id = models.CharField(max_length=50, null=True, blank=True)
	class Meta:
		app_label = 'admin_app'



class Admins(AbstractUser):
	first_name = models.CharField(max_length = 50, null=True, blank=True)
	last_name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(max_length=13, blank=True, null=True)
	password = models.CharField(max_length=200, null=True, blank=True)
	address = models.TextField(null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	state = models.CharField(max_length=30, null=True, blank=True)
	zip = models.CharField(max_length=20, blank=True)
	country = models.CharField(max_length=30, null=True, blank=True)
	status = models.CharField(max_length=30, null=True, blank=True)
	last_login = models.DateTimeField(null=True)
	first_login = models.DateTimeField(null=True)
	role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, null=False, blank=False)



	objects = UserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		app_label = 'admin_app'
		verbose_name = ('user')
		verbose_name_plural = ('users')
		indexes = [
			models.Index(fields=['email', 'username'])
		]

	def check_password(self, raw_password):
		return check_password(raw_password, self.password)

	def hash_password(self, raw_password):
		hash_password = make_password(raw_password)
		return hash_password

	def save(self, *args, **kwargs):
		# if not self.username:
		# 	self.username = self.email
		super(Admins, self).save(*args, **kwargs)

	def __str__(self):
		try:
			return self.first_name+' '+self.last_name
		except(Exception)as e:
			return self.email


@receiver(post_save, sender=Admins)
def create_hashed_password(sender, instance=None, created=False, **kwargs):
	if created:
		hash_password = make_password(instance.password)
		user = Admins.objects.filter(id=instance.id).first()
		user.password = hash_password
		# user.customer_id = random.randint(0,1000000)
		user.save()


