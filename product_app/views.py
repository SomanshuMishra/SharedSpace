from django.shortcuts import render
from django.http import HttpResponse
from product_app.models import *
from product_app.serializers import *

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
from django.core import serializers



class DepartMentView(GenericAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Department Registered Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error During Department Data', 'status_code':400, 'status':False, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Request data needed' ,'status_code':400, 'status':False},status=400)
    
    def get(self,request):
        department = Department.objects.all().values()
        return JsonResponse({'message':'All Department ', 'status':True, 'status_code':200,'departments':list(department)}, status=200)
    
    def put(self,request):
        id = request.data['id']
        data = request.data['data']
        department = Department.objects.filter(pk=id).first()
        if department:
            serializer = DepartmentSerializer(department,data=data)
            if serializer.is_valid():
                serializer.save()            
                return JsonResponse({'message':'Department Updated ', 'status':True, 'status_code':200,'updated data':serializer.data}, status=200)
            return JsonResponse({'message':'Wrong Data Format ', 'status':False, 'status_code':400}, status=400)
            return JsonResponse({'message':'No Department of this id ', 'status':False, 'status_code':400}, status=400)
        
    def delete(self,request):
        id = request.data['id']
        print(id,'ID')
        print(id,'ID')
        print(id,'ID')
        print(id,'ID')
        if id:
            department = Department.objects.filter(dept_id=id)
            print(department)
            department.delete()
            return JsonResponse({"message":"Department Deleted Successfully", 'status':True, 'status_code':200}, status=200)
        return JsonResponse({'message':'No id given ', 'status':False, 'status_code':400}, status=400)
        
    
class AttributeAddView(GenericAPIView):
    serializer_class = AttributeSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = AttributeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Attribute Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding attribute', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Attribute Data required', 'status':False, 'status_code':400}, status=400)
    
class AttributeValueView(GenericAPIView):
    serializer_class = AttributeValueSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = AttributeValueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Attribute Value Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding attribute value', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Attribute Value Data not given', 'status':False, 'status_code':400}, status=400)
    
class ProductValueApiView(GenericAPIView):
    serializer_class = ProductAttributeSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = ProductAttributeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Product Attribute Value Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding Product  attribute value', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Attribute Value Data not given', 'status':False, 'status_code':400}, status=400)
    
class ProductApiView(GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Product Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding Product  ', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Product  Data not given', 'status':False, 'status_code':400}, status=400)
    
class ProductStatusApiView(GenericAPIView):
    serializer_class = ProductStatusSerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = ProductStatusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Product Status Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding Product Status  ', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Product Status Data not given', 'status':False, 'status_code':400}, status=400)
    
class ProductCategoryApiView(GenericAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = (AllowAny,)
    def post(self,request):
        if request.data:
            serializer = ProductCategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message':'Product Category  Added Successfully', 'status':True, 'status_code':200}, status=200)
            return JsonResponse({'message':'Error during adding Product category  ', 'status':False, 'status_code':400, 'errors':serializer.errors}, status=400)
        return JsonResponse({'message':'Product category Data not given', 'status':False, 'status_code':400}, status=400)
    
