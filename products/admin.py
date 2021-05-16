from django.contrib import admin
from products.models import SKU
from products.models import SPU
from products.models import SKUSpec
from products.models import SpecName
from products.models import SpecOption
from products.models import Topic
from products.models import TopicSKU
from products.models import Banner
from django.utils.html import format_html

from django.utils.safestring import mark_safe

class SpecNameInline(admin.StackedInline):
    model = SpecName

class SpecOptionInline(admin.StackedInline):
    model = SpecOption

class TopicSKUInline(admin.StackedInline):
    model = TopicSKU

class SPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [
        SpecNameInline,
        SpecOptionInline
    ]

class SKUSpecInline(admin.TabularInline):
    model = SKUSpec

class SKUAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description','image_data')
    inlines = [
        SKUSpecInline
    ]
    def image_data(self,obj):
        return format_html(
            '<img src="{}" width="156px" height="98px"/>',
            obj.list_pic.url,
        )

class TopicAdmin(admin.ModelAdmin):
    inlines = [
        TopicSKUInline
    ]



admin.site.register(SKU,SKUAdmin)
admin.site.register(SPU,SPUAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Banner)
header = admin.AdminSite.site_header = 'hahahahha'

# Register your models here.
