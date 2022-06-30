"==============CRUD================"
# Create - создать
# Read - прочитать
# Update - обновить
# Delete - удалить
from utils import validate_id, read_db, write_to_db

database = read_db("db.json")


database = {
    296: {'name': 'Бекзат', 'password': 'скала', 'info': '...'}, 
    134: {'name': 'Эртай', 'password': 'пароль', 'info': '...'}, 
    987: {'name': 'Оомат', 'password': 'Кыргызстан', 'info': '...'}, 
    273: {'name': 'Имран', 'password': '12345', 'info': '...'}, 
    596: {'name': 'Жийде', 'password': 'return', 'info': '...'}, 
    514: {'name': 'Манас', 'password': 'Маке', 'info': '...'}, 
    912: {'name': 'Арафат', 'password': '54321', 'info': '...'}, 
    801: {'name': 'Элжаз', 'password': 'парол', 'info': '...'}, 
    518: {'name': 'Гулсана', 'password': '312', 'info': '...'}, 
    366: {'name': 'Эркайым', 'password': 'Айдин', 'info': '...'}, 
    861: {'name': 'Бекназ', 'password': 'Арёль', 'info': '...'}, 
    599: {'name': 'Эдиль', 'password': 'ьлорап', 'info': '...'}, 
    567: {'name': 'Айгул', 'password': 'май', 'info': '...'}, 
    394: {'name': 'Закир', 'password': '@@@', 'info': '...'}, 
    672: {'name': 'Бегайым', 'password': 'makers', 'info': '...'}, 
    182: {'name': 'Мырзайым', 'password': 'Bootcamp2221', 'info': '...'}, 
    770: {'name': 'Даниэл', 'password': 'covid19', 'info': '...'}, 
    420: {'name': 'Жибек', 'password': '1404', 'info': '...'}, 
    556: {'name': 'Калысбек', 'password': 'стол', 'info': '...'}, 
    570: {'name': 'Ырыс', 'password': 'suuuuuuuuiiiiiiiiiiii', 'info': '...'}, 
    954: {'name': 'Айканыш', 'password': 'qwerty', 'info': '...'}, 
    149: {'name': 'Арген', 'password': '11172332', 'info': '...'}, 
    267: {'name': 'Нурмухамед', 'password': 'Не верный', 'info': '...'}, 
    209: {'name': 'Бектур', 'password': '0101', 'info': '...'}, 
    731: {'name': 'Алан', 'password': 'душу питона', 'info': '...'}, 
    718: {'name': 'Куба', 'password': '1', 'info': '...'}, 
    653: {'name': 'Жаангер', 'password': 'ох блин', 'info': '...'}, 
    405: {'name': 'Богдан', 'password': 'Кудайберген', 'info': '...'}, 
    698: {'name': 'Айгерим', 'password': 'синий маркер', 'info': '...'}, 
    744: {'name': 'Настя', 'password': 'Python21', 'info': '...'}, 
    689: {'name': 'Жаркынай', 'password': 'Мафия', 'info': '...'}
}

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
