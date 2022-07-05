from shop.models import Product, Category
from shop.serializers import ProductSerializer

cat = Category('Phones')
obj1 = Product("iphone", 234, "...", 3, cat)
obj2 = Product("lenovo", 134, "...", 5, cat)
obj3 = Product("samsung", 34, "...", 10, cat)
res = ProductSerializer().serialize_queryset([obj1, obj2, obj3])
from pprint import pprint
pprint(res)