from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet

router = routers.DefaultRouter()
router.register('categories',   CategoryViewSet)
router.register('orders',       OrderViewSet)
router.register('products',     ProductViewSet)
router.register('customers',    CustomerViewSet)
router.register('orderitems',    OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]