
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from products.models import SKU
from products.models import SPU
from products.serializers import SKUSerializer, SPUSerializer, RelatedSKUSerializer

# Create your views here.
class SKUViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer

class RelatedSKUViewSet(viewsets.ModelViewSet):
    queryset = SKU.objects.all()
    serializer_class = RelatedSKUSerializer
