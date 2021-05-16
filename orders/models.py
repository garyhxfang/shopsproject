from django.db import models
from django.utils.html import format_html
from products.models import SKU
# Create your models here.



class Order(models.Model):
    '''
    ORDER_STATUS_ENUM = [
        (1,'待付款'),
        (2,'待发货'),
        (3,'待收货'),
        (4,'待评价'),
        (5,'已完成'),
        (6,'已取消')
    ]
    PAYMENT_METHOD_ENUM = [
        (1,'微信支付')
        (2,'货到付款')
    ]
    '''
#    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="下单用户")
#    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES,  verbose_name="订单状态")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="总金额")
    
    def __str__(self):
        return str(self.id)
    '''
    total_count = models.IntegerField(default=1, verbose_name="商品总数")
    products_amount = models.DecimadescriptionlField(max_digits=10, decimal_places=2, verbose_name="商品金额")
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="优惠金额")
    freight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="运费金额")
    payment_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, verbose_name="支付方式")
    consignee = models.CharField(max_length=32, verbose_name="收件人")
    phone = models.CharField(max_length=14, verbose_name="联系电话")
    address = models.CharField(max_length=100, verbose_name="收货地址")
    create_time = models.DateTimeField(verbose_name="创建时间")
    modify_time = models.DateTimeField(verbose_name="修改时间")
    confirm_time = models.DateTimeField(verbose_name="确认时间")
    payment_time = models.DateTimeField(verbose_name="付款时间")
    deliver_time = models.DateTimeField(verbose_name="发货时间")
    arrival_time = models.DateTimeField(verbose_name="到货时间")
    receive_time = models.DateTimeField(verbose_name="收货时间")
    timeout_time = models.DateTimeField(verbose_name="超时时间")
    '''


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='skus', on_delete=models.CASCADE, verbose_name="订单")
    sku = models.ForeignKey(SKU, on_delete=models.PROTECT, verbose_name="订单商品")
    def __str__(self):
        return str(self.sku)
    
    '''
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    count = models.IntegerField(default=1, verbose_name="数量")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    '''
   
