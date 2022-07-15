from urls import urlpatterns
from pprint import pprint
from shop.views import cars_create, cars_listing, cars_delete, cars_retrieve, cars_update
cars_create()
cars_create()
cars_update(0)
cars_retrieve(0)
cars_listing()
cars_delete(1)

while True:
    try:
        url, arg = input("Введите адрес: ").split("/")
    except ValueError:
        print("Enter a valid url")
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)