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

# Create your views here.

class AdminRegisterApiView(GenericAPIView):
	serializer_class = AdminSerializer
	permission_classes = (AllowAny,)
	def post(self, request):
		if request.data:
			admin = Admins.objects.filter(email=request.data.get('email', None)).last()
			print(admin)
			if not admin:
				serializer = AdminSerializer(data=request.data)
				if serializer.is_valid():
					serializer.save()
					return JsonResponse({'message':'Admin Registered Successfully', 'status':True, 'status_code':200}, status=200)
				return JsonResponse({'message':'Error During Registerin Data', 'status_code':400, 'status':False, 'errors':serializer.errors}, status=400)
			return JsonResponse({'message':'Admin Alredy Exists, please try with defernt email id', 'status':False, 'status_code':400}, status=400)
		return JsonResponse({'message':'Invalid Data', 'status_code':400, 'status':False}, status=400)




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


class ChangePasswordView(APIView):
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