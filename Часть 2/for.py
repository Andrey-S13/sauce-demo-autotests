# List comprehension:
[x for x in collection if condition]

# Обычный цикл:
result = []
for x in collection:
    if condition:
        result.append(x)  # ← вот этот x!



students = ["Alex", "Ivan", "Olga", "Semen", "Igor", "Svetlana"]

# К каждому элементу из списка Students применяем переменную f
for f in students:
    # Далее, что мы хотим сделать с переменной f. К примеру вывести на печать:
     print(f)


students = ["Андрей", "Саша", "Петр", "Ольга", "Марина"]
for f in students:
    var = "Инженер " + f # Новая переменная var содержит конкатенацию фразы "Инженер" с переменной f из цикла for
    print(var)


students = ["Андрей", "Саша", "Петр", "Ольга", "Марина"]
for f in students: # Наш цикл for начнет присваивать переменной f значения каждого элемента из списка по очереди (1-ая итерация, 2-ая и т.д. = круги цикла)
    if f == "Петр": # Как только значение переменной f будет равно "Петр", начнет срабатывать данный участок кода (ниже, где сдвиг)
        var = "Инженер " + f
        print(var) # Результат: Инженер Петр


students = ["A", "B", "C", "D", "E"]
for f in students[:3]:
    print(f) # Результат: А В С. Внимание: значение будут считаться 0, 1, 2, а "3" крайнее, входить не будет !!!


students = ["000", "111", "222", "333", "444"]
for f in students[1:3]:
    print(f) # Результат: 111 222


students = ["Andrey", "Boris", "Ilya"]
for f in students:
    print(len(f))
# Наш цикл for присваивает значения каждого элемента из списка и выводит на экран его длину символов через функцию len
    # Результат: 6 5 4


numbers = list(map(int, input().split()))

for i in numbers:
    if i % 2 == 0:
        print(i)
# Даны числа от 1 до 20
# Вывод: четные 2, 4, 6 и т.д.


numbers = list(map(int, input().split()))
count = 0

for number in numbers:
    if number % 2 == 0:
        count += number
print(count)
# Даны числа от 1 до 20
# Вывод: сумма четных чисел


films = input().split()
for i, film in enumerate(films):
    print(f'Индекс {i}: {film}')
# Дан список фильмов
# Вывести отдельно в формате "Индекс _: фильм"


# Решение 1
count_letters = 0
summary_words = 0

films = input().split()
for film in films:
    for letter in film:
        count_letters += 1
summary_words += count_letters
print(summary_words)
# Суммировать все элементы из списка названия фильмов

# Решение 2 - убирается вложенный цикл for и заменяется функцией len(). Складываются сразу длины слов из списка
summary_words = 0

films = input().split()
for film in films:
    summary_words += len(film)
print(summary_words)


numbers = list(map(int, input().split()))

for i, number in enumerate(numbers):
    if i % 2 != 1:  # четный индекс
        print(number)
# Вывести элементы списка с четными индексами


# Решение 1
numbers = list(map(int, input().split()))

count = 0
iteration_count = 0

for number in numbers:
    count += number
    iteration_count += 1
average = count / iteration_count
print(average)
# Найти среднее арифметическое число из списка чисел

# Решение 2
numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)  # Sum - сумма всех числел, len - количество чисел
print(average)


# Решение 1 - через функцию isalpha - проверка содержания букв
a = input()

for element in a:
    if element.isalpha():  # True / False
        print(element)
# Вывсти на печать только буквы

# Решение 2 - через фильтрацию
a = input()

for element in filter(str.isalpha, a):
    print(element)


a = input()
b = input()
count = 0

for char in a:
    if b == char:    # сравниваем b с текущим символом char
        count += 1
print(count)
# Выводим значение "a" (слово: цифры/буквы) и ищем по элементу "b" кол-во повторений в слове "а"


# Решение 1
a = input()
count = 0

for char in a:
    if "b" == char or "a" == char or "i" == char:
        count += 1
print(count)
# Вывести общую цифру суммы встречающихся символов "a, b, i" в слове "a"

# Решение 2 - лаконичное
a = input()

count = 0
for char in a:
    if char in "abi":  # Содержит ли символ ввода "а" в строке "abi" (ab, abi, a, b и т.д.)
        count +=1
print(count)


# Решение 1
list = []
list.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # добавление множества значений в список
for list in range(1,6):
    print(list)
# В пустой список добавили значения от 1 до 10 и вывели на печать первые 5 значений

# Решение 2
list = []
for i in range(1, 11):
    list.append(i)  # добавление значений в список по одному
for list in range(1,6):
    print(list)


numbers_1 = list(map(int, input().split()))
numbers_2 = list(map(int, input().split()))

count_1 = sum(numbers_1)
count_2 = sum(numbers_2)

if count_1 >= count_2:
    print("1")
else:
    print("2")
# Дано 2 списка. Вывести 1 и 2, если сумма 1-го списка больше или 2-го.


# Решение 1
list = [1, 2.5, 5, 7, 8, 3.9]

list_new = [x for x in list if x == int(x)]
list = [x for x in list if x != int(x)]  # Или x == float(x)

print(list_new)
print(list)
# Из текущего списка сделать два: 1) int-список и 2) float-список

# Решение 2
numbers = [1, 2.5, 5, 7, 8, 3.9]

list_int = []
list_float = []

for i in numbers:
    if type(i) == int:
        list_int.append(i)
    elif type(i) == float:  # Можно заменить "else:"
        list_float.append(i)
print(list_int)
print(list_float)