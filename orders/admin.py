from django.contrib import admin
from orders.models import Order
from orders.models import OrderProduct

admin.site.register(Order)
admin.site.register(OrderProduct)
# Register your models here.
