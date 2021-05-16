from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from Cryptodome.PublicKey import RSA
from base64 import b64encode
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256
from . import wechatpay
from orders.models import Order
from orders.models import OrderProduct
from orders.serializers import OrderSerializer
from orders.serializers import OrderProductSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

class Checkout1 (APIView):
    def post(self, request, format=None):
        order = request.data
        skus = request.data['skus']
        serialzer = OrderSerialzer(data=order)
        if serialzer.is_valid():
            serialzer.save()
        order_id = serialzer.data['id']

        for sku in skus:
            sku['order']=order_id
            serialzer = OrderProductSerialzer(data=sku)
            if serialzer.is_valid():
                serialzer.save()
        return HttpResponse("Success")

class Checkout2 (APIView):
    def post(self,request,format=None):
        serializer = OrderSerializer(data=request.data)
        print(repr(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return HttpResponse('error')

class Checkout (generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderViewSet (viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    








@api_view(['GET'])
def appid(request):
    if request.method == "GET":
        url = 'https://api.weixin.qq.com/sns/jscode2session'
        appid = 'wxe228b2d8087cd3f0'
        secret = '8a7d176bb551845b47c23d7cc75d7963'
        js_code = request.query_params['code']
        grant_type = 'authorization_code'

        body = {
            'appid' : appid,
            'secret' : secret,
            'js_code' : js_code,
            'grant_type' : grant_type
        }
        r = requests.get(
            url, 
            params = body 
            )

        print(js_code)
        print(r)
        return Response(r)


@api_view(['POST'])
def pay(request):
    if request.method == "POST":
        r=wechatpay.create_payment_order(request)
        return Response(r)

