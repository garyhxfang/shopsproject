from products.models import SKU
from products.models import SPU
from rest_framework import serializers

class SKUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SKU
        fields = ['id','name','price']

class SPUSerializer(serializers.HyperlinkedModelSerializer):
    skus = SKUSerializer(read_only=True,many=True)
    class Meta:
        model = SPU
        fields = ['id','skus']

class RelatedSKUSerializer(serializers.HyperlinkedModelSerializer):
    spu = SPUSerializer(read_only=True)
    class Meta:
        model = SKU
        fields = ['id','spu']

