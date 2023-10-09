from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

from .serializers import CategorySerializer, ProductSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer

from .models import Category, Product, Customer, Order, OrderItem

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

@require_GET
@csrf_exempt
def order_total_by_customer(request):
# Получаем сумму заказов для каждого пользователя
    customers = Customer.objects.all()
    
    results = []

    # Заполняем словарь результатами
    for customer in customers:
        dic = {
            "id": customer.id,
            "name": customer.name,
            "LTV" : customer.life_time_value()
        }
        results.append(dic)    
    # Возвращаем результат в формате JSON
    return JsonResponse(results, safe=False)

@require_GET
@csrf_exempt
def count_first_child_categories(request):
    # Получаем все категории, у которых нет родительских категорий
    root_categories = Category.objects.filter(parent=None)

    # Получаем количество дочерних категорий для каждой корневой категории
    child_category_counts = root_categories.annotate(child_count=Count('category'))

    result = []
    # Выводим результаты
    for category in child_category_counts:
        result.append(CategorySerializer(category).data)
    return JsonResponse(result, safe=False)