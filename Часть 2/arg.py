def function_name():
    """Краткое описание функции.

    Подробное описание, если нужно.
    """
    # код функци


# Позиционный аргумент
def description(name, age, sex):
    print(f"Имя {name}, Возраст {age}, Пол {sex}")

description("Аnna", 30, "man") # Позиционный аргумент = все идет по порядку
Имя Anna, Возраст 30, Пол man


# Именованный аргумент
def description(name, age, sex):
    print(f"Имя {name}, Возраст {age}, Пол {sex}")

description(sex="Аnna", name=30, age="man") # Именованный аргумент = агрумент может выбираться любым
# Имя 30, Возраст man, Пол Аnna


# Смешанный тип агрументов
n = "Anna"
a = 30
def description(name, age, sex):
    print(f"Имя {name}, Возраст {age}, Пол {sex}")

description(n, a, "man") # Смешанный тип агрументов
# Имя Anna, Возраст 30, Пол man


# Примеры определения переменной. Решение 1
def new_function():
    num = int(input())
    if num % 2 == 0:
        print("Good")
    else:
        print("Bad")

new_function()  # Вызов после определения
# 5
# Bad

# Решение 2
def new_function(num):
    if num % 2 == 0:
        print("Good")
    else:
        print("Bad")

new_function(num = int(input()))
# 10
# Good


def new_function():
    var = input()
    for char in var[::-1]:
        print(char, end='')

new_function()
# Привет
# тевирП


def new_function():
    """Подсчитывает количество гласных букв в введенном слове"""  # docstring с описанием функции
    vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']  # vowel - гласные; consonants - согласные
    word = input()
    count = 0

    for letter in word:
        if str(letter).lower() in vowel:
            count += 1
    print(count)


new_function()

# Программирование
# 7 (гласных)


def new_function():
    numbers = list(map(int, input().split()))

    new_numbers = sorted(numbers, reverse=True)
    if new_numbers[0] == new_numbers[1]:
        print("Bad")
    else:
        print(new_numbers[1])


new_function()

# 1 3 4 8 2 1 - вывести 2 по величине число из списка
# 4


def new_function():

    words = input().split()
    uniqe = []

    for word in words:
        if word not in uniqe:
            uniqe.append(word)

    for j in uniqe:
        print(j)


new_function()

# Привет Hello 12 Hello - вывести уникальные значения
# Привет
# Hello
# 12


# Решение 1
def new_function():
    radius = int(input())
    pi = 3.14

    square_circle = pi * radius ** 2
    print(int(square_circle))


new_function()

# Решение 2
def new_function(radius, pi = 3.14):

    square_circle = pi * radius ** 2
    print(int(square_circle))


new_function(int(input()))

# 10
# 314

# Решение 1
def new_function(text):
    print(f"{text} любит Python")


new_function(text = input())

# Сергей
# Сергей любит Python

# Решение 2
def new_function(name, text='любит Python'):
    print(f"{name} {text} ")


new_function(input())


def new_function(text):
    print(text.replace(" ", ""), end='')


new_function(input())

# Весь Мир театр
# ВесьМиртеатр

# Решение 1
def new_function(number):
    if number < 0:
        print(number * (-1))
    else:
        print(number)


new_function(int(input()))

# -1
# 1

# Решение 2
def new_function(number):
    print(abs(number))


new_function(int(input()))


# Решение 1 - некрасивое
def new_function():
    num_1, num_2, num_3 = int(input()), int(input()), int(input())
    if num_1 <= num_3:
        print('Bad')
    else:
        print('Good')


new_function()

# Решение 2 - оптимальное

def new_function(numbers):
    print('Good' if numbers[0] > numbers[-1] else 'Bad')


new_function([input() for i in range(3)])


# Решение 1 - отвратительное
def new_function(email):
    if '@' in email:
        if '.ru' in email:
            print('Good')
        else:
            print('Bad')
    else:
        print('Bad')


new_function(input())

# test.ru@mail
# Bad
# test@mail.ru (идет @ и потом .ru)
# Good

# Решение 2 - получне + комбинированное
def new_function(email: str):
    if "@" in email and email.endswith(".ru") and email.index("@") < email.index(".ru"):  #Излишне сравнивать элементы, но для примера (использовать можно отдельно)
        print("Good")
    else:
        print("Bad")



new_function(input())


# Решение 1 - мое
# Напишите функцию new_function(), которая запрашивает у пользователя число и выводит на печать Good, если оно простое и Bad если не простое.
from math import sqrt
def new_function():

    number = int(input())

    if number == 2:  # единственное четное простое число
        print('Good')
    elif number % 2 == 0:  # исключаем четные числа
        print('Bad')
    elif number <= 1:  # исключаем числа меньше или равные 1
        print('Bad')
    else:
        for i in range(3, int(sqrt(number)) + 1, 2):  # нечетные числа от 3 до √n с шагом 2
            if number % i == 0:
                print('Bad')
                break
        else:
            print('Good')


new_function()

# Решение 2 - чужое
def new_function(value):

    new_value = int(value)
    count = 0
    div = 1

    while div <= new_value:
        if int(new_value/div) == new_value/div:  #перебор чисел от 1 до 11, пока не будет 11. Тогда счетчик count += 1
            count += 1
        div += 1
    if count == 2:
        print("Good")
    else:
        print("Bad")


new_function(input())