from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CustomerViewSet, OrderViewSet, OrderItemViewSet, order_total_by_customer, count_first_child_categories

router = routers.DefaultRouter()
router.register('categories',   CategoryViewSet)
router.register('orders',       OrderViewSet)
router.register('products',     ProductViewSet)
router.register('customers',    CustomerViewSet)
router.register('orderitems',    OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order-total-by-customer/', order_total_by_customer, name='order-total-by-customer'),
    path('count-first-child-categories/', count_first_child_categories, name='count-child-categories'),
]