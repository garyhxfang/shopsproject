from django.db import models
from django.utils.html import format_html

# Create your models here.

class SPU(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500,blank=True)
    

    def __str__(self):
        return self.name

class SKU(models.Model):
    spu = models.ForeignKey('SPU', on_delete=models.SET_NULL, related_name='skus',null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price=models.DecimalField(max_digits=10, decimal_places=2)
    for_sale = models.BooleanField(default=True)
    description = models.CharField(max_length=500, blank=True)
    link = models.URLField()
    main_pic = models.ImageField(upload_to = 'image',blank=True)
    list_pic = models.ImageField(upload_to = 'image',blank=True)
    detail_pic = models.ImageField(upload_to = 'image',blank=True)
    back_topic = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
    
 
    '''
    def image_data(self):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            self.list_pic.url,
        )
    '''

class SpecName(models.Model):
    spu = models.ForeignKey('SPU', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class SpecOption(models.Model):
    spu = models.ForeignKey('SPU', on_delete=models.CASCADE)
    spec_name = models.ForeignKey('SpecName', on_delete=models.CASCADE)
    option = models.CharField(max_length=100)


    def __str__(self):
        return self.option

class SKUSpec(models.Model):
    sku = models.ForeignKey('SKU', on_delete=models.CASCADE)
    spec = models.ForeignKey('SpecName', on_delete=models.PROTECT)
    option = models.ForeignKey('SpecOption', on_delete=models.PROTECT)
    
    def __str__(self):
        print(self.option)
        return '%s: %s' % (self.spec, self.option)

class Topic(models.Model):
    name = models.CharField(max_length=40)
    bg_pic = models.ImageField(upload_to = 'image',blank=True)
    sort_weight = models.IntegerField()
    link = models.URLField()
    def __str__(self):
        return self.name

class TopicSKU(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    sku = models.ForeignKey('SKU', on_delete=models.CASCADE)
    sort_weight = models.IntegerField()


    def __str__(self):
        return self.sku

class Banner(models.Model):
    TYPE_OPTIONS = [
        (1,'product'),
        (2,'topic')
    ]
    banner_type = models.IntegerField(choices=TYPE_OPTIONS)
    sku = models.ForeignKey('SKU', on_delete=models.CASCADE, blank=True)
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE, blank=True)
    banner_pic = models.ImageField(upload_to = 'image',blank=True)

    sort_weight =  models.IntegerField()