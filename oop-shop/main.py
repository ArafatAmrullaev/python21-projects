from shop.models import Product, Category
from shop.views import product_list, product_create, product_detail, product_delete, product_update

cat = Category('Phones')
Category('dyson')
Category('food')
obj1 = Product("iphone", 234, "...", 3, cat)
obj2 = Product("lenovo", 134, "...", 5, cat)
obj3 = Product("samsung", 34, "...", 10, cat)


from pprint import pprint

# pprint(product_create())
pprint(product_list())
# while True:
#     id_ = input('Введите id продукта: ')
#     pprint(product_detail(id_))
id_ = input('Введите продукт для обновления: ')
pprint(product_update(id_))
