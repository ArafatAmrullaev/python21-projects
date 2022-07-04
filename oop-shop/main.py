from models import User, Product, Comment

user1 = User('test@gmail.com', 'Hello', 'man')

user1.register('123456789', '123456789')
user1.login('123456789')
print(user1.is_authenticated)

product1 = Product('Iphone 12', 1223, '...', 10)
user1.logout()
comment1 = Comment(user1, product1, 'Оч классный телефон')
print(comment1)