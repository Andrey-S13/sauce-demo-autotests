a = 10
while a > 1:
    print(a)
# Бесконечный цикл, т.к. условие True

a = 10
while a >= 1:
    a -= 1  # a=a-1
    print(a)
    # Результат:
    # 10 - 1
    # 9 - 1
    # .....
    # 2 - 1
    # 1 - 1 (что удовлетворяет условию а >= 1, поэтому в ответе будет 9, 8... 2, 1, 0)

# Цикл for идеально подходит для списков
# Если для списка использовать цикл while: 1) измерить длину списка через len(), эту длину записать в переменную,
# и только потом запускать цикл.
# Подходит для одиночных операций.

count = 1
while count <= 5:
    print(count)
    count += 1
# Счетчик до 5 (ответ: от 1 до 5)


# Итерация по списку
my_list = [1, 2, 3, 4, 5]
index = 0

while index < len(my_list):
    print(my_list[index])
    index += 1
# Перебор элементов списка, пока индекс не превысит длину списка (нужно, когда работаем со списком по всем его элементам)
# Ответ: от 1 до 5


# Итерация с условием
fruits = ["apple", "banana", "orange", "grape"]
index = 0

while index < len(fruits):
    if len(fruits[index]) > 5:  # Проверка длины строки
        print(fruits[index])  # Печатаем элемент больше 5 символов
    index += 1
# Перебор элементов списка, которые удовлетворяют условиям
# Ответ: banana, orange


# Изменение списка
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    numbers[index] *= 2  # Удваиваем текущий элемент
    index += 1

print(numbers)
# Ответ: список [2, 4, 6, 8, 10]


numbers = list(map(int, input().split()))
index = 0

while index < len(numbers):
    if numbers[index] > 7:
        print(numbers[index])
    index += 1
# Вывести из списка значения больше 7


numbers = list(map(int, input().split()))
index = 0

while numbers[index] % 2 == 0 and index < len(numbers):
    print(numbers[index])
    index += 1
# Пока элементы четные в списке, цикл срабатывает


numbers = list(map(int, input().split()))
index = 0

while index < len(numbers):
    if numbers[index] % 2 == 1:
        squart = numbers[index] * numbers[index]
        print(squart)
    index += 1
# Вывод на печать всех нечетных чисел


films = input().split()
index = 0

# Цикл работает, пока элемент состоит только из букв И не достигнут конец списка
while index < len(films) and films[index].isalpha():
    print(films[index])
    index += 1


number = int(input("Введите число: "))
i = 1

print(f"Делители числа {number}:")

while i <= number:
    if number % i == 0:
        print(i)
    i += 1
# Вывести по порядку все делители числа


fuel_cur = int(input())
fuel_min = int(input())

fuel_usage = fuel_cur * 0.1
days = 0

while fuel_cur - (fuel_usage * days) > fuel_min:
    days += 1
print(days)
# Топливо 100л - макс, топливо 45л - мин. Расход 10% от макс. Найти кол-во дней расхода топлива до мин. значения


word = input()
left = 0
right = len(word) - 1
is_palindrome = True

while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)
# Является ли слово палиндромом
# level == True
# Fire == False


n = int(input())
i = 1

while i <= n:
    print(i)
    i += 1
# Вывести все значения от 1 до n


a = int(input())
b = int(input())

total = a

while a < b:
    a += 1
    total += a
print(total)
# Вывести сумму всех цифр: от 1 до 5 = 15 и т.д.


numbers = list(map(int, input().split()))
index = 0

while index < len(numbers) and numbers[index] > 7:
    print(numbers[index])
    index += 1
# Вывести ряд цифр до первой цифры меньше 7


from math import sqrt

numbers = list(map(int, input().split()))  # range (1, 100000) - можно поиграться с выводом всех простых чисел
index = 0

while index < len(numbers):
    current_num = numbers[index]  # проверяем current_num на простоту
    is_prime = True  # ← ДОЛЖНО БЫТЬ ЗДЕСЬ! Для каждого числа свой флаг

    if current_num <= 1:
        is_prime = False
    elif current_num == 2:
        is_prime = True
    elif current_num % 2 == 0:  # все четные кроме 2
        is_prime = False
    else:
        # Проверяем делители от 3 до sqrt(current_num) с шагом 2
        for i in range(3, int(sqrt(current_num)) + 1, 2):  # Или current_num**0.5
            if current_num % i == 0:
                is_prime = False
                break
    if is_prime:  # ← ЭТО ДОЛЖНО БЫТЬ ВНУТРИ ЦИКЛА
        print(current_num)
    index += 1 # ← И ЭТО ТОЖЕ ВНУТРИ ЦИКЛА
# 10 8 12 3 4 115 121
# 3




