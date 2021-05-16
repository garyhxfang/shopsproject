"""shops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from products import views as productsviews
from orders import views as ordersviews
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'skus', productsviews.SKUViewSet)
router.register(r'relatedskus', productsviews.RelatedSKUViewSet)
router.register(r'orders',ordersviews.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('appid/', ordersviews.appid),
    path('pay/', ordersviews.pay),
    path('admin/', admin.site.urls),
    path('checkout/', ordersviews.Checkout.as_view())
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)