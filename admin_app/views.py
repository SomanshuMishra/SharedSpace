from django.shortcuts import render

from admin_app.models import *
from admin_app.serializers import *

from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.contrib.auth.hashers import make_password, check_password


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework import routers, serializers, viewsets
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView
import math

from django.db.models import Q as queue

# Create your views here.

class AdminRegisterApiView(GenericAPIView):
	serializer_class = AdminSerializer
	permission_classes = (AllowAny,)
	def post(self, request):
		if request.data:
			admin = Admins.objects.filter(email=request.data.get('email', None)).last()
			if not admin:
				serializer = AdminSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Admin Registered Successfully', 'status':True, 'status_code':200}, status=200)
				return JsonResponse({'message':'Error During Registerin Data', 'status_code':400, 'status':False, 'errors':serializer.errors}, status=400)
			return JsonResponse({'message':'Admin Alredy Exists, please try with defernt email id', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Invalid Data', 'status_code':400, 'status':False}, status=400)

class AdiminCrudApiView(GenericAPIView):
	serializer_class = AdminSerializer
	def get(self, request):
		admin_id = request.GET.get('id', None)
		print(admin_id)
		if admin_id:
			admin = Admins.objects.filter(id=admin_id).last()
			if admin:
				serializer = AdminSerializer(admin)
				return JsonResponse({'message':'Admin Detail', 'status':True, 'status_code':200, 'Admin':serializer.data}, status=200)
			return JsonResponse({'message':'Admin Detail not found', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)


	def put(self, request):
		if request.data:
			admin_id = request.GET.get('id', None)
			admin = Admins.objects.filter(id=admin_id).last()
			if admin:
				serializer = AdminSerializer(admin, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Admin Detail Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Admin Detail Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Admin Detail', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)



	def delete(self, request):
		admin_id = request.GET.get('id', None)
		if admin_id:
			Del = Admins.objects.filter(id=admin_id).delete()
			return JsonResponse({"message":"Admin Detail Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)


class RolesApiView(GenericAPIView):
	serializer_class = RolesSerializer
	def post(self, request):
		if request.data:
			serializer = RolesSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'message':'Role Created Successfully', 'status':True, 'status_code':200}, status=200)
			return JsonResponse({'message':'Error During Role Creating', 'status_code':400, 'status':False, 'errors':serializer.errors}, status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)
	
	def get(self, request):
		role_id = request.GET.get('id', None)
		if role_id:
			print("role",role_id)
			role = Roles.objects.filter(id=role_id).last()
			print(role)
			if role:
				serializer =  RolesSerializer(role)
				return JsonResponse({'message':'Role', 'status':True, 'status_code':200, 'Role':serializer.data}, status=200)
			return JsonResponse({'message':'Role not found', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)


	def put(self, request):
		if request.data:
			role_id = request.GET.get('id', None)
			role = Roles.objects.filter(id=role_id).last()
			if role:
				serializer = RolesSerializer(role, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Role  Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Role  Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Role ', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def delete(self, request):
		role_id = request.GET.get('id', None)
		if role_id:
			Del = Roles.objects.filter(id=role_id).delete()
			return JsonResponse({"message":"Role  Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)



class RoleResourcesApiView(GenericAPIView):
	serializer_class = RoleResourcesSerializer
	def post(self, request):
		if request.data:
			serializer = RoleResourcesSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({'message':'Role Resource Created Successfully', 'status':True, 'status_code':200}, status=200)
			return JsonResponse({'message':'Error During Role Resource Creating', 'status_code':400, 'status':False, 'errors':serializer.errors}, status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)
	
	def get(self, request):
		role_id = request.GET.get('id', None)
		if role_id:
			print("role",role_id)
			role = RoleResources.objects.filter(id=role_id).last()
			print(role)
			if role:
				serializer =  RoleResourcesSerializer(role)
				return JsonResponse({'message':'Role Resource Detail', 'status':True, 'status_code':200, 'Resource':serializer.data}, status=200)
			return JsonResponse({'message':'Role Resource Detail not found', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)


	def put(self, request):
		if request.data:
			role_id = request.GET.get('id', None)
			role = RoleResources.objects.filter(id=role_id).last()
			if role:
				serializer = RoleResourcesSerializer(role, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Role Resource Detail Updated Successfully', 'status':True, 'status_code':204}, status=200)
				return JsonResponse({'message':'Error During Role Resource Detail Update', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'Invalid Role Resource Detail', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

	def delete(self, request):
		role_id = request.GET.get('id', None)
		if role_id:
			Del = RoleResources.objects.filter(id=role_id).delete()
			return JsonResponse({"message":"Role Resource Detail Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)

class RoleResourcesDelApiView(APIView):
	def post(self, request):
		ids = request.data.get('Ids')
		if ids:
			for i in ids:
				Del = RoleResources.objects.filter(id=i).delete()
			return JsonResponse({"message":"Role Resources Deleted Successfully", 'status':True, 'status_code':200}, status=200)
		return JsonResponse({'message':'Bad Request', 'status':False, 'status_code':400}, status=400)




class AdminLoginApiView(GenericAPIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		if request.data:
			if request.data.get('email', None) and request.data.get('password', None):
				admin = Admins.objects.filter(email=request.data.get('email', None)).first()
				if admin:
					password_status = admin.check_password(request.data.get('password', None))
					if password_status:
						serializer = AdminSerializer(admin)
						payload = jwt_payload_handler(admin)
						token = jwt_encode_handler(payload)
						return JsonResponse({'token':token, 'message':'Admin Logged In successfully', 'status_code':200, 'status':True, 'Admin':serializer.data}, status=200)
					return JsonResponse({'message':'Invalid Email or Password, Please Try Again', 'status_code':400, 'status':False}, status=400)
				return JsonResponse({'message':'Admin Doesn\'t Exists', 'status_code':400, 'status':False}, status=400)
			return JsonResponse({'message':'Email and Password Required', 'status_code':400, 'status':False},status=400)
		return JsonResponse({'message':'Bad Request', 'status_code':400, 'status':False}, status=400)



class LogoutApiView(GenericAPIView):
	def get(self, request):
		return JsonResponse({'message':'Logged Out Successfully', 'status':True, 'status_code':200}, status=200)


from django.core.mail import EmailMultiAlternatives


class ForgotPasswordLinkView(GenericAPIView):
	permission_classes = (AllowAny,)
	def get(self, request):
		email = request.GET.get('email')
		admin = Admins.objects.filter(email=email).first()
		if admin:
			payload = jwt_payload_handler(admin)
			token = jwt_encode_handler(payload)
			if token:
				reset_link = 'https://planaheadvip.com/admin/#/reset-password/'+token+'/'+email
				try:
					self.forgot_password_mail([email, reset_link])
				except Exception as e:
					print(e)
					return JsonResponse({'message':'Error during sending mail, please contact support', 'status':False, 'status_code':500}, status=500)
				return JsonResponse({'message':'Password reset email sent to the respective email-id, please check email', 'status':True, 'status_code':200, 'email':email}, status=200)
			return JsonResponse({'message':'Error During generating token, please contact support or else try again letter', 'status':False, 'status_code':500}, status=500)
		return JsonResponse({'message':'Invalid Email, admin not found. Please check email-id register or no.', 'status':False, 'status_code':400}, status=400)

	def forgot_password_mail(self, args):
		email = args[0]
		reset_link = args[1]
		text_content = "Password Reset Link - "+reset_link
		rendered = '<div>You have requested for password reset, To reset password click here - {0}</div>'.format(reset_link)
		frm = self.get_from_email()
		print(frm)
		msg = EmailMultiAlternatives('Password Reset Link', text_content, frm, [email])
		msg.attach_alternative(rendered, "text/html")
		msg.send()

	def get_from_email(self):
		# app_conf = AppConfiguration.objects.filter(key_name='from_email_id').last()
		# if app_conf:
		# 	if app_conf.key_value:
		# 		return app_conf.key_value
		return 'PlanAhead<postmaster@mg.planaheadvi>'



class ForgotPasswordChangePasswordView(GenericAPIView):
	def post(self, request):
		email = request.data.get('email')
		password = request.data.get('password')
		admin = Admins.objects.filter(email=email).first()
		if admin:
			admin.password = make_password(password)
			admin.save()
			return JsonResponse({'message':'Password Reseted Successfully', 'status_code':200, 'status':True}, status=200)
		return JsonResponse({'message':'Invalid Email', 'status':False, 'status_code':404}, status=404)


class ChangePasswordView(GenericAPIView):
	def post(self, request):
		old_password = request.data.get("old_password")
		password = request.data.get('password')
		email = request.data.get('email')
		admin = Admins.objects.filter(email=email).first()
		if admin:
			if admin.check_password(old_password):
				admin.password = make_password(password)
				admin.save()
				return JsonResponse({'message':'Password Changed Successfully', 'status_code':200, 'status':True}, status=200)
			return JsonResponse({'message':'Sorry, you provided wrong current password', 'status_code':400, 'status':False}, status=200)
		return JsonResponse({'message':'Invalid Email', 'status':False, 'status_code':404}, status=404)


class AdminListApiView(APIView):
	def get(self, request):
		page = request.GET.get('page', 1)
		end = int(page)*50
		start = end-50
		sortby = request.GET.get('sortby')
		oder = request.GET.get('Order')
		if sortby:
			if (oder=="Desc"):
				c = "-"+sortby
			else:
				c = sortby
		else:
			c = '-id'
		status = request.GET.get('status', None)
		query = request.GET.get('search', None)
		if query:
			search = query.isspace()
			result = []
			if ' ' in query:
				new_query = query.split()
				result = Admins.objects.filter(queue(first_name__icontains=new_query[0],last_name__icontains=new_query[1])).order_by(c)[start:end]
				if result:
					serializer=AdminSerializer(result, many=True)
					total_count = Admins.objects.filter(queue(first_name__icontains=new_query[0],last_name__icontains=new_query[1])).count()
					page_count = math.ceil(total_count/50)
					return JsonResponse({'message':'Admin', 'status':True, 'status_code':200, 'Admin':serializer.data, 'total_count':total_count, 'total_pages':page_count}, status=200)
				return JsonResponse({'message':'data not found', 'status':False, 'status_code':400}, status=400)
			else:
				result = Admins.objects.filter(queue(id__icontains=query) | queue(first_name__icontains=query) | queue(last_name__icontains=query) | queue(email__icontains=query) | queue(phone_number__icontains=query) | queue(username__icontains=query) | queue(password__icontains=query) | queue(address__icontains=query) | queue(city__icontains=query) | queue(state__icontains=query) | queue(country__icontains=query) | queue(status__icontains=query) | queue(zip__icontains=query)).order_by(c)[start:end]
				if result:	
					serializer=AdminSerializer(result, many=True)
					total_count = Admins.objects.filter(queue(id__icontains=query) | queue(first_name__icontains=query) | queue(last_name__icontains=query) | queue(email__icontains=query) | queue(phone_number__icontains=query) | queue(username__icontains=query) | queue(password__icontains=query) | queue(address__icontains=query) | queue(city__icontains=query) | queue(state__icontains=query) | queue(country__icontains=query) | queue(status__icontains=query) | queue(zip__icontains=query)).count()
					page_count = math.ceil(total_count/50)
					return JsonResponse({'message':'Admin', 'status':True, 'status_code':200, 'Admin':serializer.data, 'total_count':total_count, 'total_pages':page_count}, status=200)
				return JsonResponse({'message':'data not found', 'status':False, 'status_code':400}, status=400)
			return JsonResponse({'message':'data not found', 'status':False, 'status_code':400}, status=400)
		elif status:
			Admin = Admins.objects.filter(status=status).order_by(c)[start:end]
			count = Admins.objects.filter(status=status).count()
			page_count = math.ceil(count/50)
			if Admin:
				serializer = AdminSerializer(Admin, many=True)
				return JsonResponse({'message':'Admin', 'status':True, 'status_code':200, 'Admin':serializer.data, 'total_count':count, 'total_pages':page_count}, status=200)
			return JsonResponse({'message':'status not found', 'status':False, 'status_code':400}, status=400)
		else:
			Admin = Admins.objects.all().order_by(c)[start:end]
			count = Admins.objects.count()
			page_count = math.ceil(count/50)
			if Admin:
				serializer = AdminSerializer(Admin, many=True)
				return JsonResponse({'message':'all Admin', 'status':True, 'status_code':200, 'Admin':serializer.data, 'total_count':count, 'total_pages':page_count}, status=200)
			return JsonResponse({'message':'Admin not found', 'status':False, 'status_code':400}, status=400)




