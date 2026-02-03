# -*- coding: utf-8 -*-

try-except
Нужно для обработки исключений в Python

try - блок кода, который может исключание
except - блок кода, который будет выполнен, если исключение возникло

try:
    # Код, который может вызвать исключение
except ExceptionType:
    # Код, который будет выполнен, если исключание возникло

ExceptionType - это тип исключения, который обрабатывается


a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))

result = int(a / b) #Для вывода целых значений int
print("Результат : " + str(result)) #т.к. это конкатенация, тип данных str

# ZeroDivisionError - исключение. На ноль делить нельзя (1/0)



a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))
try:
    result = int(a / b)
    #Для вывода целых значений int
except ZeroDivisionError:
    result = 0
    # Вводим, чтобы не было ошибки незаданной переменной в print
    print("На 0 делить нельзя")
print("Результат : " + str(result))
#т.к. это конкатенация, тип данных str

# Покажем, что код продолжает работу, добавив новую переменную с функцией:

result_2 = a + b
print(result_2)

# Ответ:
# Введите первое значение: 1
# Введите второе значение: 2
# Результат : 0
# 3




try:
    a = int(input("Введите первое значение: "))
    b = int(input("Введите второе значение: "))
    result = int(a / b)
    print('result = ', result)
    # Поместили переменные и функцию в оператора
except(ValueError):
    print("Error. Wrong symbols")
except(ZeroDivisionError):
    print("Error. Dividing by zero")


var = input()

try:
    number = int(var)
    print(number)
except:
    print("Невозможно преобразовать строку в целое число")
# Преобразовать значение в целое число





num_1 = int(input("1-е число: "))
num_2 = int(input("2-е число: "))

try:
    result = num_1 / num_2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("На ноль нельзя делить")

# 1-е число: 1
# 2-е число: 0
# На ноль нельзя делить


try:
    # Код, который может вызвать исключение
finally:
    # Код, который будет выполнен всегда


num_1 = int(input("1-е число: "))
num_2 = int(input("2-е число: "))

try:
    result = num_1 / num_2
    print(f"Ответ: {result}")
finally:
    print("Всего хорошего")
# 1-е число: 1
# 2-е число: 0
# Всего хорошего
# ZeroDivisionError


num_1= int(input("Введите первое число: "))
num_2= int(input("Введите второе число: "))


try:
    result = num_1 / num_2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("На ноль делить нельзя")
finally:
    print("До скорых встреч")
# Введите первое число: 1
# Введите второе число: 0
# На ноль делить нельзя
# До скорых встреч


my_list = [10, 20, 30, 40, 50]
num_index = input()

try:
    print(my_list[int(num_index)])
except IndexError:
    print("Индекс вне диапазона")


var_1 = input()
var_2 = input()

my_list = [0, 2, 4]

try:
    result = my_list[int(var_1)] / my_list[int(var_2)]
    print("Good")
except ZeroDivisionError:
    print("Деление на ноль недопустимо")
except IndexError:
    print("Индекс вне диапазона")


var = input()

string_list = ['10', '20', 'abc']

try:
    result = string_list[int(var)]
    if int(result):
        print("Good")
except ValueError:
    print("Неверный символ для типа int")
    print("Bad")
except IndexError:
    print("Индекс вне диапазона")
    print("Bad")


var = input()

try:
    if int(var) in [1, 2, 3]:
        print(int(var))
    else:
        print("Некорректный ввод")
except ValueError:
    print("Некорректный ввод")