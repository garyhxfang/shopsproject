from rest_framework import serializers
from orders.models import Order
from orders.models import OrderProduct



class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['sku']

class OrderSerializer(serializers.ModelSerializer):
    skus = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['total_amount','skus']
    def create(self, validated_data):
        products_data = validated_data.pop('skus')
        print(products_data)
        order = Order.objects.create(**validated_data)
        for sku in products_data:
            OrderProduct.objects.create(order=order,**sku)
            print(sku)
        return order

        