"==============CRUD================"
# Create - создать
# Read - прочитать
# Update - обновить
# Delete - удалить
from utils import validate_id, read_db, write_to_db

database = read_db("db.json")

def read(u_id, update=False):
    """
    Принимает id юзера
    Выводит его имя и информацию
    Если такого юзера нет, вызывается Exception
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]['name']
    info = database[u_id]['info']
    sex = database[u_id]['sex']
    if update:
        print(f""" 
        ============Updated{u_id}=============
        Name: {name}
        Sex: {sex}
        Info: {info}
        ============================
        """)
    else:
        print(f""" 
        ============={u_id}=============
        Name: {name}
        Sex: {sex}
        Info: {info}
        ============================
        """)

def create():
    """ 
    Запрашивает данные о пользователе
    Записывает в бд
    """
    from utils import generate_id, validate_passwords
    name = input('Введите имя: ')
    password = input('Введите пароль: ')
    password2 = input('Подтвердите пароль: ')
    validate_passwords(password, password2)
    info = input('Введите информацию о вас: ')
    sex = input('Укажите пол (м, ж): ')
    id_ = generate_id(database.keys())
    database[id_] = {
        'name': name,
        'password': password,
        'info': info,
        'sex': sex
    }
    print('Вы были успешно добавлены в Python21')
    write_to_db("db.json", database)
    return id


def delete(u_id):
    """
    Принимает id пользователя
    Если юзер существует, он удаляется из базы данных
    Если юзер нет, вызывается ошибка 
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]['name']
    sex = database[u_id]['sex']
    del database[u_id]
    if sex == 'м':
        print(f'Юзер {name} был успешно удалён')
    else:
        print(f'Юзер {name} была успешно удалена')
    write_to_db("db.json", database)

def update(u_id):
    """
    Принимает id юзера
    Выводит старые данные
    Принимает новые данные
    Изменяет в базе данных 
    """
    validate_id(database.keys(), u_id)
    read(u_id)
    # Принимает новые данные
    name = input('Введите имя: ')
    info = input('Введите информацию о вас: ')
    sex = input('Укажите пол (м, ж): ')
    # изменяем бд
    database[u_id]['name']
    database[u_id]['info']
    database[u_id]['sex']
    read(u_id)
    write_to_db("db.json", database)
