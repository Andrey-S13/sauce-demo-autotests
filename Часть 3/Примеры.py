# -*- coding: utf-8 -*-

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний треугольник")
elif a == b or a == c or b == c:
    print("Равнобедренный треугольник")
elif a + b == c or a + c == b or b + c == a:
    print("Прямоугольный треугольник")
else:
    print("Разносторонний треугольник")
# list = [1, 2, 3] - Разносторонний треугольник
# list = [2, 2, 3] - Равнобедренный треугольник
# list = [3, 3, 3] - Равносторонний треугольник
# list = [3, 6, 9] - Прямоугольный треугольник


'''Вам необходимо проводить суммирование квадратов двух ближайших пар чисел, до тех пор пока они 
не будут больше 100 и вывести два данных числа на печать.'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
var = int()
for i in range(0, len(numbers),2):
        var = numbers[i]**2 + numbers[i+1]**2
        # print(f"{var} test_print")
        if var > 100:
            print(f"{numbers[i]}\n{numbers[i + 1]}")
            break
        i += 1

# 7
# 8



'''
Выведите все элементы списка, которые больше предыдущего элемента.

Например:
1, 3, 2, 1, 4, 10, 5, 3

3 больше 1, выводим на печать 3
2 меньше 3, ничего не выводим на печать
1 меньше 2, ничего не выводим на печать
4 больше 1, выводим на печать 4
'''

numbers = list(map(int, input().split()))
# numbers = [1, 3, 2, 1, 4, 10, 5, 3]

for i in range(0, len(numbers)-1):
    # print(i+1)
    if numbers[i] < numbers[i+1]:
        print(numbers[i+1])
    i += 1

# 3
# 4
# 10


'''
Посчитает и выведет на печать какое количество зёрен будет на шахматной доске, если класть на каждую следующую
клетку доски вдвое больше зёрен, чем на предыдущую, начиная с одного.
В нашем распоряжении две доски: классическая 64 клетки и мини-доска 16 клеток, код должен корректно работать для
каждого варианта
'''

# Решение 1
num = int(input())
count = 0

for i in range(1, num+1):
    formula = 2**(i-1)
    count += formula
print(count)

# 64
# 18_446_744_073_709_551_615 - 18 квинтиллионов 446 квадриллионов 744 триллиона 73 миллиарда 709 миллионов 551
# тысяча 615

# Решение 2:
n = int(input())
a = 1
for i in range(n):
    a *= 2
print(a-1)


'''
Каждый товар дешевеет на 1% от вчерашней стоимости. Подсчитайте стоимость товара на десятый день
и выведите число на печать в виде целого числа:
1 день - 1 000 000
2 день - 990 000
3 день - 980 100
..........................
10 день - X (913517)
'''

a = int(input())

formula = a * 0.99**(10-1)  # первый день не считается, остается 9 дней
print(int(formula))

# 1_000_000
# 904382


'''
Напишите код, который принимает на входе баланс пользователя в виде целого числа.
В магазине акция:
Стоимость 1 пакета молока = 100 рублей
2 пакета молока - скидка 30%
3 пакета молока - скидка 40%
5 пакета молока- скидка 50%
Посчитайте количество товара, которые может купить пользователь для каждой акции
'''

a = int(input())  # balance_user

one_milk = a / 100  # price = 100
print(int(one_milk))
two_milks = (a/0.7) // (100 * 2)
print(int(two_milks * 2))
three_milks = (a/0.6) // (100 * 3)
print(int(three_milks * 3))
three_milks = (a/0.5) // (100 * 5)
print(int(three_milks * 5))


# 1000
# 10
# 14
# 15
# 20


'''
Напишите код, который на входе принимает список со строками, через пробел.
Выведите на печать даты, которые относятся к високосному году.
'''

new_list = input().split()
# new_list = ['01.12.2000', '5.05.1992', '11.11.2011', '8.09.1521']


for i in new_list:
    year = i[-4:]
    year_int = int(year)
    if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
        print(i)


# 01.12.2000 5.05.1992 11.11.2011 8.09.1521
# 01.12.2000
# 5.05.1992


'''
Напишите код, который на входе принимает список с названием адресами почти пользователей через пробел.
Создайте два списка, в первый поместите адреса из Ru сегмента, во второй остальные.
Далее выведите на печать оба новых списка, сперва Ru, затем остальные
'''

# email = input().split()
email = ['test@mail.ru', 'python@yandex.ru', 'login@gmail.com']
email_ru = []
email_other = []

for i in email:
    if '.ru' in i:
        email_ru.append(i)
    else:
        email_other.append(i)

print(email_ru)
print(email_other)



# test@mail.ru python@yandex.ru login@gmail.com
#
# ['test@mail.ru', 'python@yandex.ru']
# ['login@gmail.com']


'''
Напишите код, который на входе принимает список с url адресами через пробел.
Выведите на печать имена сайтов
'''

url = input().split()  # Universe resource locator

for i in url:
    if i.startswith('http'):
        # remove protocol
        if i.startswith('https://'):
            clean = i[8:]  # remove 'https://'
        else:
            clean = i[7:]  # remove 'http://'

        if clean.startswith('www.'):
            clean = clean[4:]  # remove 'www.'

        domain = clean.split('/')[0]
        print(domain)

# https://www.yandex.ru https://www.google.com/search http://www.yan.ru
# yandex.ru
# google.com
# yan.ru


'''
Напишите код, который на входе принимает список с url адресами через пробел.
Выведите на печать имя сайта, которое встречается чаще всего.
'''

from collections import Counter

url = input().split()
# url = ['https://www.yandex.ru', 'https://www.google.com/search', 'http://www.yan.ru', 'https://www.yandex.ru']
domain_list = []

for i in url:
    if i.startswith('http'):
        # remove protocol
        if i.startswith('https://'):
            clean = i[8:]  # remove 'https://'
        else:
            clean = i[7:]  # remove 'http://'

        if clean.startswith('www.'):
            clean = clean[4:]  # remove 'www.'

        domain = clean.split('/')[0]
        domain_list.append(domain)

counter = Counter(domain_list)

print(max(counter))

# https://www.yandex.ru https://www.google.com/search http://www.yan.ru https://www.yandex.ru
# yandex


'''
Напишите код, который на входе принимает список с буквами, через пробел. Каждая буква имеет свой порядковый номер, например a = 1, б=2, в=3 и т.д.
Посчитайте сумму всех букв и вывести на печать число
'''
# Решение 1
letter = input().split()
# letter = 'abcde'
orders_letters = {}
count = 0

for i in range(0, len(letter)):
    symbol = letter[i]
    orders_letters[symbol] = i+1
# print(orders_letters)
for value in orders_letters.values():
    count += int(value)
print(count)

# abcde
# 1 + 2 + 3 + 4 + 5 = 15


# Решение 2
letters = input().split()
print(sum(range(1, len(letters) + 1)))

# abcde
# 1 + 2 + 3 + 4 + 5 = 15

# Создание словаря через цикл for:
alphabet = 'абвгд'
orders_letters = {}
for i, letter in enumerate(alphabet, 1):
    orders_letters[letter] = i
print(orders_letters)

# {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5}

# Создание словаря
# alphabet = 'абвгд'
# orders_letters = {letter: i for i, letter in enumerate(alphabet, 1)}
# print(orders_letters)

# {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5}


'''
Напишите код, который на входе принимает список с именами сотрудников, через пробел. Часть данных сотрудников уже имеет нумерацию, нумерация может состоять ТОЛЬКО ИЗ ЦИФР.
Выведите на печать всех пронумерованных сотрудников
'''

new_list = input().split()

for i, employee in enumerate(new_list):
    if employee[0].isdigit() and not employee[1].isalpha():
        print(employee)

# Иван 1.Алексей 3)Ольга 1а.Анна в2)Семен
# 1.Алексей
# 3)Ольга


language = 'Русский'

if language != 'English' != 'Espa?ol':
    print('Язык по умолчанию не является ни английским, ни испанским')

if language != 'English' != 'Русский':
    print('Язык по умолчанию не является ни английским, ни русским')

# Язык по умолчанию не является ни английским, ни испанским
# Язык по умолчанию не является ни английским, ни русским  - второе выводится, т.к. сравнивается (1 и 2) и (2 и 3)









'''
Напишите код, который на входе принимает список с именами сотрудников, через пробел и строку с именем сотрудника
Необходимо осуществлять проверку наличия имени сотрудника в данном списке, без учета регистра верхней буквы.
'''

new_list = input().split()
name = input()

lower_list = [item.lower() for item in new_list]
if name.lower() in lower_list:
    print('Good')
else:
    print('Bad')

# Иван алексей ольга Анна Семен
# Иван
# Good


'''
Это ИНН, который может содержать 10 или 12 цифр. Если длина числа 10 или 12 цифр, то выводим на печать Good,
если любое другое, то Bad.
'''


inn = input()

if inn.isdigit() and (len(inn) == 10 or len(inn) == 12):
    print('Good')
else:
    print('Bad')

# 2345963878 - Good
# 123456789 - Bad


'''
Напишите код, который принимает одно значение в виде строки, которое содержит 11 цифр и может содержать знак +.
Необходимо преобразовать данную строку в матрицу телефонного номера и затем вывести на печать.
Матрицы телефонного номер
+7 (999) 999-99-99    - обратите внимание, что по обеим сторонам скобок стоит один пробел
'''

# Решение 1
number = input()
number = number.replace("+", "")

if len(number) == 11:
    mask_number = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:9]}-{number[9:12]}"
    print(mask_number)


# 89234567890
# +7 (923) 456-78-90

# Решение 2

s = [x for x in input() if x.isdigit()]
result = '+7 (XXX) XXX-XX-XX'
for digit in s[1:]:
    result = result.replace('X', digit, 1)

print(result)


'''
Напишите код, который принимает одно значение в виде строки, которое содержит дату.
Необходимо преобразовать данную строку в шаблон даты и затем вывести на печать.
Шаблон даты
05.12.2021 - обратите внимание, что день и месяц даты должны иметь вид двухзначного числа.
'''

data = input()

first_dot = data.find('.')
second_dot = data.find('.', first_dot + 1)

# Поиск позиций

day = data[:first_dot]
if len(day) != 2:
    day = f"0{day}"
    print(day)

month = data[first_dot + 1: second_dot]
if len(month) != 2:
    month = f"0{month}"
    print(month)

year = data[second_dot + 1:]

# Еще можно применить "Разделение на части":
# data = '1.1.2011'
# SplitElements = data.split('.')  # ['1', '1', '2011']
# day, month, year = SplitElements[0], SplitElements[1], SplitElements[2]
# print(day, month, year)  # 1 1 2011

data_mask = f"{day}.{month}.{year}"

print(data_mask)

# 1.1.2011
# 01.01.2011


'''
Необходимо вывести его содержимое по образцу:
Ключ - Значение, обратите внимание, что с обеих сторон от тире идет пробел
'''

# Решение 1
data = {'a': 10, 'b': 20, 'c': 15}

dataValues = data.values()
maxValue = max(dataValues)

for key, value in data.items():
    if value == maxValue:
        print(f"{key} - {value}")

# Решение 2

data = {'a': 10, 'b': 20, 'c': 15}

result = max(data.items(), key=lambda value: value[1])
print(*result, sep=' - ')  # если не поставить *, то будет ответ в виде ('b', 20). *result - распаковывает кортеж
# на отдельные аргументы
'''
lambda v: v[1] - это анонимная функция
Лямбда-функция эквивалентна:
def get_value(pair):
    return pair[1]

для кортежа ('a', 10):
v[0] = 'a' (key)
v[1] = 10 (value)
'''

# b - 20


'''
Отсылка к лямбде-функции (наглядный пример):
'''
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Сортировка по оценкам с помощью лямбды
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Решение 1

# keys = input().split()
keys = ['a', 'b', 'c']
# values = input().split()
values = [1, 2, 3]

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

# {1: 'a', 2: 'b', 3: 'c'}

# Решение 2
my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print(my_dict)

# {1: 'a', 2: 'b', 3: 'c'}

for key, value in my_dict.items():
    print(f"{key} - {value}")

# a - 1
# b - 2
# c - 3

# Решение 3

my_dict = dict(zip(keys, values))

for key, value in my_dict.items():
    print(f"{key} - {value}")

# a - 1
# b - 2
# c - 3


'''
Напишите код, который принимает одно значение в виде строки.

Проведите сверку, которая проверяет, существует ли заданный ключ в словаре. Если присутствует, то вывести на печать Good, если нет, то Bad.

data = {'a': 1, 'b': 2, 'c': 3}

Используйте для ввода строчи key = input()
'''
data = {'a': 1, 'b': 2, 'c': 3}
key = input()

if key in data:
    print("Good")
else:
    print("Bad")