def identification(name):
    print("You are")

    if name == "Andrey":
        print("Student")

    else:
        print("Teacher")

name = input("Input your name: ")
identification(name)
# Input your name: Andrey
# You are
# Student


def identification(name):
    print("You are")

    if name == "Andrey":
        result = "Student"

    else:
        result = "Teacher"

    return result

name = input("Input your name: ")
print(identification(name))

# Input your name: afd
# You are
# Teacher


def identification(name):
    print("You are")

    if name == "Andrey":
        result = "Student"

    else:
        result = "Teacher"

    return result

name = input("Input your name: ")

n = "Alex "
s = identification(name)
print(n + s)

# Input your name: Student
# You are
# Alex Teacher


def identification(name):
    print("You are")

    if name == "Andrey":
        result = "Student"

    else:
        result = "Teacher"

    return result

def status(result):
    print(result)

name = input("Input your name: ")
result = 5
status(identification(name))

# Input your name: Alex
# You are
# Teacher


def sum_1(a,b):
    result = a + b
    print(f"Первая сумма равна {result}")

sum_1(5,3)
# Первая сумма равна 8

'''Return - это оператор, который возвращает результат своего выполнения. Позволяет передавать данный из функции
обратно в вызывающий код. Делает функции более гибкими и полезными'''

def name_funcion(arguments):
    # code
    return result_code


def sum_1(a,b):
    sum = a + b
    return sum
print(f"It's: {sum_1(4,6)}")
# It's: 10
def sum_1(a,b):
    sum = a + b
    return sum
print(f"It's: {sum_1(4,6)}")
# It's: 10
def sum_2(c,d):
    sum = c + d
    return sum
print(f"It's: {sum_2(14,24)}")
# It's: 38
print(f"It's: {sum_2(4,4) + sum_1(4,4)}")
# It's: 16

# Функции, которые принимают значения из других
def sum_1(a,b):
    sum = a + b
    return sum
def sum_2(c,d):
    sum = c + d
    return sum
def mega_sum(f,g):
    result = f + g
    return result
print(f"Sum of numbers is: {mega_sum(sum_1(1,2), sum_2(3,4))}")
# Sum of numbers is: 10


# Функция, которая возвращает несколько значений
def name():
    name_1 = "Alex"
    name_2 = "Dmitry"
    return name_1, name_2

user_name_1, user_name_2 = name()
print(user_name_1, user_name_2)
# Alex Dmitry


'''         Примеры          '''

def new_function():

    var = int(input())
    if 1 <= var <= 3 and var % 2 == 0:
        return "Два"
    elif 4 <= var <= 6 and var % 2 == 1:
        return "Пять"
    else:
        return 'Bad'


result = new_function()

print(result)
# 7
# Bad
# 2
# Два


constant=7
def new_function(var):

    if var % constant == 0:
        return "Good"
    else:
        return 'Bad'


result = new_function(int(input()))

print(result)
# 5
# Bad
# 7
# Good


def logic():

    var = int(input())

    if var % 2 == 0:
        return even()
    else:
        return odd()

def even():
    return "ЧЕТ"
def odd():
    return "НЕЧЕТ"


result = logic()

print(result)
# 4
# ЧЕТ
# 7
# НЕЧЕТ


# Решение 1
def new_function():

    FIO = input().split()
    return FIO[1]

result = new_function()

print(result)
#
# Решение 2
'''В принте только input, остальное описано в функции + для 1 случая переменная не нужна'''
def new_function(string):

    return string.split()[1]


print(new_function(input()))


# Решение 1
def new_function(string):  # Список создается внутри функции

    FIO = string.split()

    Familia = FIO[0]

    for i in FIO[1]:
        Imya = i[0]
        break

    for j in FIO[2]:
        Otchestvo = j[0]
        break

    return f"{Familia} {Imya}.{Otchestvo}."  # Вывод: Фамилия И.О.

result = new_function(input())

print(result)
# Суворов Андрей Дмитриевич
# Суворов А. Д.

# Решение 2
def new_function(string):  # Список создается внутри функции
    FIO = string.split()

    Familia = FIO[0]
    Imya = FIO[1][0]  if len(FIO) > 1 else ""
    Otchestvo = FIO[2][0] if len(FIO) > 2 else ""

    if Otchestvo:
        return f"{Familia} {Imya}.{Otchestvo}."  # Вывод: Фамилия И.О.
    else:
        if Imya:
            return f"{Familia} {Imya}."  # Вывод: Фамилия И.
        else:
            return f"{Familia}"  # Вывод: Фамилия


result = new_function(input())

print(result)
# Суворов Андрей Дмитриевич > Суворов А. Д.
# Суворов Андрей > Суворов А.
# Суворов > Суворов


# Решение 1
def new_function(name, born_in, current_year = 2024):

    age = current_year - born_in

    return f"Меня зовут {name}, мне {age}."


result = new_function(input(), int(input()))

print(result)
# Andrey
# 1995
# Меня зовут Andrey, мне 29.

# Решение 2
def new_function(name, year):
    return f"Меня зовут {name}, мне {2024 - year}."

print(new_function(input(), int(input())))
# Adam
# 2024
# Меня зовут Adam, мне 0.


def logic(name, country):

    if country in russia():  # Можно еще через сравнение строк: "if country == russia():"
        return f"Здравствуй {name}"
    elif country in england():
        return f"Hello {name}"

def russia():
   return 'Россия'

def england():
    return 'England'


result = logic(input(), input())

print(result)
# Леха + Россия
# Здравствуй Леха
# Alex + England
# Hello Alex


# Решение - 1 (некрассивое)
def logic(name, country): # Если страна РФ, вызывается функция РФ с присвоением вводимого имени туда

    if country == 'Россия':  # Если РФ - чтение из russia.txt
        russia(name)
        with open('doc/russia.txt', 'r', encoding='utf-8') as fr_ru:
            text_ru = fr_ru.read()
            return text_ru
    elif country == 'England':  # Чтение из england.txt
        england(name)
        with open('doc/england.txt', 'r', encoding='utf-8') as fr_eng:
            text_eng = fr_eng.read()
            return text_eng


def russia(name):  # Запись имени в russia.txt
    if name:
        with open('doc/russia.txt', 'w', encoding='utf-8') as fw_ru:
            fw_ru.write(name)



def england(name):  # Запись имени в england.txt
    if name:
        with open('doc/england.txt', 'w', encoding='utf-8') as fw_eng:
            fw_eng.write(name)


result = logic(input(),input())  # Переменные для функции logic

print(result)
# Леха + Россия
# файл "russia.txt" с содержимым "Леха"
# Alex + England
# файл "england.txt" с содержимым "Alex"

# Решение - 2
def logic(name, country):

    if country == 'Россия':
        return russia(name)

    elif country == 'England':
        return england(name)


def russia(name):
        with open('doc/russia.txt', 'w') as fw:
            fw.write(name)
        with open('doc/russia.txt', 'r') as fr:
            return fr.read()


def england(name):
    with open('doc/england.txt', 'w') as fw:
        fw.write(name)
    with open('doc/england.txt', 'r') as fr:
        return fr.read()


print(logic(input(),input()))


def new_function(days, balance):

    if (1 <= days <= 3) and (balance >= 30):
        with open('doc/file.txt', 'w') as fw:
            for i in range(1, days+1):
                text = f"{i} день - баланс {balance - i * 7 + 7} - списалось 7 - осталось {balance - i * 7}\n"
                fw.write(f"{text}")
        with open('doc/file.txt', 'r') as fr:
            result_1 = fr.read()
            print(result_1)
    else:
        print('Bad')


new_function(int(input()), int(input()))
# 3
# 40
# 1 день - баланс 40 - списалось 7 - осталось 33
# 2 день - баланс 33 - списалось 7 - осталось 26
# 3 день - баланс 26 - списалось 7 - осталось 19
# 4
# 10
# Bad


def new_function():
    balance = int(input())
    transfer_money = int(input())

    if balance > transfer_money:
        operation = balance - transfer_money
        return operation
    elif balance == transfer_money:
        return "0"
    else:
        text = "Не хватает денежных средств"
        return text


result = new_function()

print(result)
# 100
# 100
# 0


def new_function(guest_food, guest_tea):
    if guest_food < guest_tea:
        return "Bad"

    total_money = (guest_food * 3000) + (guest_tea * 500)
    return total_money

print(new_function(int(input()), int(input())))
# 10
# 5
# 32500


