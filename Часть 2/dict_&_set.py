# Список - выдает все элементы по порядку. Если большой массив данных и нужжно работать с каждым эл-ом (вне зависимости, повторяется элемент или нет)
# Чтобы объявить список, ставим []

family_1 = ["Andrey", "Stas", "Olga", "Semen", "Anna", "Andrey"]
print(family_1)
# ['Andrey', 'Stas', 'Olga', 'Semen', 'Anna']

# Множества - выдает хаотично значения. Большой массив данных и нужна сортировка (использовать только одиночные)

family_2 = {"Andrey", "Stas", "Olga", "Semen", "Anna", "Andrey"}
print(family_2)
# {'Olga', 'Anna', 'Andrey', 'Stas', 'Semen'} - выводит только уникальные значения множества


# Словарь (ключ: значение)

family_3 = {"Father": "Andrey", "Mother": "Nasty", "Daughter": "Olga", "Son": "Semen", "Sister": "Anna"}
print(family_3["Father"])
# Andrey

family_3 = {"Father": "Andrey", "Mother": "Nasty", "Daughter": "Olga", "Son": "Semen", "Sister": "Anna"}
# Объявляем цикл for. Пишем 2 переменных: k = key (ключ), v = variable (значение). Берем 2 переменных в нашем словаре family_3 и
# подключаем функцию items, которая обозначает "элементы"
# мы хотим, чтобы цикл for прошелся по нашему словарю, прошел по всем нашим ключам, по всем значениям и вывел на печать
# все ключи нашего словаря, т.е. "маму", "папу" и т.д.
for k, v in family_3.items(): # k - key, v - variable (цикл прошелся по всем значениям, вывел все ключи)
    print(k)
# Father Mother Daughter Son Sister

family_3 = {"Father": "Andrey", "Mother": "Nasty", "Daughter": "Olga", "Son": "Semen", "Sister": "Anna"}
for k, v in family_3.items():
    print(v)
# Andrey Nasty Olga Semen Anna

family_3 = {"Father": "Andrey", "Mother": "Nasty", "Daughter": "Olga", "Son": "Semen", "Sister": "Anna"}
for k, v in family_3.items():
    print(k + " - " + v)
# Father - Andrey
# Mother - Nasty
# Daughter - Olga
# Son - Semen
# Sister - Anna


# # список
# family_1 = ["Alex", "Andrey", "Anna", "Sergey", "Alex"]
# print(family_1)
#
# # множество:
# family_2 = {"Alex", "Andrey", "Anna", "Sergey", "Alex"}
# print(family_2)
#
# # словарь
# family_3 = {"father": "Alex", "mother":"Anna", "Son":"Andrey"}
# # print(family_3["father"])
# for k, v in family_3.items():
#     print(k)
#
# # ['Alex', 'Andrey', 'Anna', 'Sergey', 'Alex'] - словарь
# # {'Alex', 'Sergey', 'Andrey', 'Anna'} - множество
# # Alex - значение ключа father

person = {
    "name": "Alex",
    "age": 30,
    "city": "SPB"
}
print(person)
# Создание словаря


name_person = person["name"]
print(name_person)
# Доступ к элементам словаря через создание отдельной переменной
# Alex


print(person["name"])  # вывод на печать через обращение к ключу
# Alex


print(person.get("age"))  # вывод на печать через обращение к ключу через метод get()
# 30


person["email"] = "suvorov@mail.com" # Добавление нового ключа в словарь и его значение
print(person)
# {'name': 'Alex', 'age': 30, 'city': 'SPB', 'email': 'suvorov@mail.com'} - первоначальный словарь остался неизменным


person = {
    "name": "Andrey",
    "age": 30,
    "city": "MSK",
    "email": "suvorov@mail.com"
}
print(person)
# {'name': 'Andrey', 'age': 30, 'city': 'MSK', 'email': 'suvorov@mail.com'}


person["email"] = "suvorov_andrey@mail.com"  # Изменяем содержимое ключа
print(person)
# {'name': 'Andrey', 'age': 30, 'city': 'MSK', 'email': 'suvorov_andrey@mail.com'}


del person["city"]  # Удаление ключа city
print(person)
# {'name': 'Andrey', 'age': 30, 'email': 'suvorov_andrey@mail.com'}


# 1. Получение списка ключей: dictionary.keys()

person = {
    "name": "Andrey",
    "age": 30,
    "city": "Moscow"
}

keys = person.keys()
print(keys)
# dict_keys(['name', 'age', 'city'])

# Второй вариант через цикл for
for key in person.keys():
    print(key)
# name
# age
# city


if "age" in person.keys():
    print("Ключ age есть в словаре")
# Ключ age есть в словаре


# Получение списка значений: dictionary.values()

values = person.values()
print(values)
# dict_values(['Andrey', 30, 'Moscow'])


for value in person.values():
    print(value)
# Andrey
# 30
# Moscow


if 30 in person.values():
    print("Значение 30 есть в словаре")
# Значение 30 есть в словаре


# Получение списка пар ключ-значение: dictionary.items()

items = person.items()
print(items)
# dict_items([('name', 'Andrey'), ('age', 30), ('city', 'Moscow')])


for key, value in person.items():
    print(f"Key: {key}, Value: {value}")
# Key: name, Value: Andrey
# Key: age, Value: 30
# Key: city, Value: Moscow


# Проверка ключ-значение:
if ("name", "Andrey") in person.items():
    print("Пара ('name', 'Andrey') присутствуют в словаре")
# Пара ('name', 'Andrey') присутствуют в словаре


new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}

for key, value in new_dict.items():
    if value > 100:
        print(key)
# file3.txt
# file4.txt
# file6.txt


new_dict = {'Имя': 'Светлана', 'Пароль': 'qwer1234', 'Код': 1984}

for key, value in new_dict.items():

    if key == "Имя":
        masked_name = value[0] + "#" * (len(value) - 1)
        print(f"{masked_name}")

    elif key == "Пароль":
        masked_password = "#" * (len(value))
        print(f"{masked_password}")

    elif key == "Код":
        code_str = str(value)
        masked_code = "#" * (len(code_str) - 1) + code_str[-1]
        print(f"{masked_code}")

# Имя: С#######
# Пароль: ########
# Код: ###4


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict_new1 = (dict1|dict2)

for key, value in dict_new1.items():
    print(f'{key} - {value}')
# Вывести в форме:
# a - 1
# b - 3
# c - 4


#Решение 1
dict1 = {'a': 1, 'b': 2, 'c': 3}

for key, value in dict1.items():
    print(f'{value} - {key}')
# 1 - a
# 2 - b
# 3 - c

# Решение 2
dict1 = {'a': 1, 'b': 2, 'c': 3}

dict2 = dict(map(reversed, dict1.items()))  # Реверсивный порядок "ключ = значение" > "значение - ключ"
for k, v in dict2.items():
    print(f'{k} - {v}')

# 1 - a
# 2 - b
# 3 - c

______

# Множества - неупорядоченная коллекция уникальных элементов, которая поддерживает операции объединения, пересечения и разности.

colors = set(["red", "green", "blue"])
# or
colors = {"red", "green", "blue"}

print(colors)
# {'red', 'blue', 'green'}


# Добавление и удаление элементов

colors.add("yellow")
print(colors)
# {'green', 'red', 'yellow', 'blue'}


# Удаление элементов

colors.remove("blue")
print(colors)
# {'red', 'green', 'yellow'}

# Основные операции с множествами

colors_1 = {"red", "green", "blue"}
colors_2 = {"yellow", "green", "blue"}

# Объединение | (сложение двух множеств, выводятся только уникальные элементы. В множестве нет дублей)

print(colors_1 | colors_2)
# {'yellow', 'blue', 'red', 'green'}


# Пересечение & (вывод элементов, которые есть в обоих множествах)

print(colors_1 & colors_2)
# {'blue', 'green'}


# Второй метод intersection()

result = colors_1.intersection(colors_2)
print(result)
# {'green', 'blue'}


# Разность (результат, который содержится в первом множестве, но отсутствует во втором множесте

print(colors_1 - colors_2)
# {'red'}

# Симметрическая разность ^ (вывод элементов из первого и второго множества за вычетом дублей)

print(colors_1 ^ colors_2)
# {'yellow', 'red'}


numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))


numbers_3 = numbers_1&numbers_2  # вывод элементов, которые есть в обоих множествах или метод "intersection()"
final = sorted(numbers_3)
for i in final:
    print(i)

# Выведите их пересечение, то есть значения которые есть в обоих множествах, в порядке возрастания
# 13 7 9 2
# 3 5 7 9

# 7
# 9


numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))

numbers_3 = numbers_1|numbers_2  # # сложение уникальных элементов, которые есть в обоих множествах
final = sorted(numbers_3)
for i in final:
    print(i)

# Объедините и выведите их на печать, в порядке возрастания
# 1 2 3 4
# 3 4 5 6

# 1
# 2
# 3
# 4
# 5
# 6


# Решение 1
numbers_1 = {1, 2, 3, 4}
numbers_2 = {4, 7, 5, 6}
# set(map(int, input().split()))

result = numbers_1.intersection(numbers_2)
if len(result) == 0:
    print('Bad')
else:
    print('Good')
# Проведите сверку двух множеств, если они имеют общие элементы, то выведите на печать Good, если нет, то Bad
# True

# Решение 2
numbers_1 = {1, 2, 3, 4}
numbers_2 = {9, 0, 5, 6}
# set(map(int, input().split()))

result = numbers_1.intersection(numbers_2)
print(result)
if not result:
    print('Bad')  # пустое множество = False
else:
    print('Good')
# False


# решение 1
# Проведите проверку данных множеств, в случае наличия элемента, который есть во всех трех множествах, то вывести на печать Good, если нет, то Bad.
numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

if not (numbers_1 & numbers_2 & numbers_3):
    print("Bad")
else:
    print("Good")
# 1 2 3
# 4 5 3
# 6 7 3
# Good

# Решение 2 (метод intersection())
numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

if not numbers_1.intersection(numbers_2, numbers_3):
    print("Bad")
else:
    print("Good")
# 1 2 3
# 4 5 6
# 7 8 9
# Bad


numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))
# numbers_1 = {1, 2, 3, 4}
# numbers_2 = {1, 4, 5, 6}
# numbers_3 = {4, 5}

numbers_4 = numbers_1.intersection(numbers_2)
print(numbers_4)  # первые два множеста имеют объединения

if numbers_1.intersection(numbers_2) != '':
    answer = numbers_4 - numbers_3  # что из 3 множества не вошло в объединение 1 и 2
    for i in answer:
        print(i)
# Выводите на печать элемент, который присутствует в первых двух, но отсутствует в третьем.
# 1