file_name = 'doc/file.txt'
data = "Hello World"

# fw = open(file_name, 'w')
# fw.write(data)
# fw.close()

with open(file_name, 'w') as files:
    files.write(data)
    # не надо закрывать файл

# Чтение файла
with open(file_name, 'r') as file:
    content = file.read()
    print(content)

# Запись в файл
with open(file_name, 'w') as file:
    file.write('Hello Ocean')

# Добавление данных в файл
with open(file_name, 'a') as file:
    file.write('\nHello Earth')  # \n - добавляет пробел

с with удобно - закрывается файл, даже если произошло исключение. Помогает избезать утечек
ресурсов и гарантирует, что файл всегда будет корректно


# fw = open('doc/file_3.txt', 'a')
# data = 'Checking 123'
# fw.write(data)
# fw.close()

file_name = 'file.txt'
data = 'Hello world'

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'a') as files:
    files.write(data)
    #Hello world


# Записываем числа в файл
with open('doc/file.txt', 'w') as file:
    for i in numbers:
        file.write(f'{i}\n')

# Читаем числа из файла и суммируем их
with open('doc/file.txt', 'r') as file:
    for line in file:
        number = int(line.strip())  # Преобразуем строку в число
        count += number
        print(f"Добавлено: {number}, Текущая сумма: {count}")
    print(f"Итоговая сумма: {count}")

# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно. Затем прочтите содержимое файла и выведите на печать сумму всех элементов файла.
# 1 2 3 4 5
# 15


# Получаем числа из ввода
numbers = list(map(int, input().split()))

# Записываем числа в file_1.txt построчно
with open('file_1.txt', 'w') as file_1:
    for i in numbers:
        file_1.write(f'{i}\n')

# Читаем file_1.txt и копируем нечетные строки в file_2.txt
with open('file_1.txt', 'r') as file_1:
    lines = file_1.readlines()  # читаем все строки

# Записываем нечетные строки в file_2.txt
with open('file_2.txt', 'w') as file_2:
    for i in range(0, len(lines), 2):  # берем каждую нечетную строку (индексы 0, 2, 4...)
        file_2.write(lines[i])

# Читаем и выводим содержимое file_2.txt
with open('file_2.txt', 'r') as file_2:
    content = file_2.read()
    print(content.strip())  # strip() убирает лишние переносы в конце

# 12 16 8 9 21
# 12
# 8
# 21


films = input().split()
# Матрица Скала Западня Бэтман

with open('doc/file_1.txt', 'w') as file_1:
    for i in films:
        file_1.write(f'{i}\n')
# Читаем первый файл
with open('doc/file_1.txt', 'r') as file_1:
    content = file_1.readlines()
    print(content)
# ['Матрица\n', 'Скала\n', 'Западня\n', 'Бэтман\n']

with open('doc/file_2.txt', 'w') as file_2:
    # Сортируем весь список content
    sorted_content = sorted(content)
    for i, film in enumerate(sorted_content):
        file_2.write(film)

with open('doc/file_2.txt', 'r') as file_2:
    content_3 = file_2.read()
    print(content_3.strip())
# Бэтман
# Западня
# Матрица
# Скала


numbers = list(map(int, input().split()))
# 12 16 8 9 21

with open('doc/file_1.txt', 'w') as file_1:
    for i in numbers:
        file_1.write(f'{i}\n')
# Читаем первый файл
with open('doc/file_1.txt', 'r') as file_1:
    content = file_1.readlines()
    # print(content)
# ['12\n', '16\n', '8\n', '9\n', '21\n']

with open('doc/file_2.txt', 'w') as file_2:
    # Преобразуем строки в числа, сортируем как числа, затем обратно в строки
    number_list = [int(line.strip()) for line in content]
    sorted_numbers = sorted(number_list, reverse=True)
    for number in sorted_numbers:
        file_2.write(f'{number}\n')

with open('doc/file_2.txt', 'r') as file_2:
    content_3 = file_2.read()
    print(content_3.strip())

# 21
# 16
# 12
# 9
# 8


# Решение 1 без оболочки "запись в файл"

films = input().split()
film_count = {}
# Скала Западня Бэтман Западня Западня Бэтман

for film in films:
    if film in film_count:
        film_count[film] += 1  # Увеличиваем счетчик для этого фильма
    else:
        film_count[film] = 1  # Добавляем фильм в словарь со значением 1

items_list = []
for film, count in film_count.items():
    items_list.append((count, film))  # Помещаем количество первым

# Сортируем по убыванию количество (первый элемент кортежа)
items_list.sort(reverse=True)

# Вывод
for film_name, film_count in items_list:
    print(f"{film_count} - {film_name}")

# '3' - Западня
# '2' - Бэтман
# '1' - Скала


# Решение 2 с оболочкой "запись в файл"

# функция split() отделяет значения и формирует список с ними, как показано ниже
# films = input().split()
films = ['Скала', 'Западня', 'Бэтман', 'Западня', 'Западня', 'Бэтман']
film_count = {}
# Скала Западня Бэтман Западня Западня Бэтман

# Записываем в файл НАЗВАНИЯ фильмов (не счетчики)
with open('doc/file_1.txt', 'w', encoding='utf-8') as file_1:
    for film in films:
        if film in film_count:
            film_count[film] += 1  # Увеличиваем счетчик для этого фильма
        else:
            film_count[film] = 1  # Добавляем фильм в словарь со значением 1

        file_1.write(film + '\n')
        # Скала
        # Западня
        # Бэтман
        # Западня
        # Западня
        # Бэтман

# Чтение из файла и подсчет частоты слов
film_count_from_file = {}  # Новый словарь для подсчета из файла

with open('doc/file_1.txt', 'r', encoding='utf-8') as file_1:
    content = file_1.readlines()
    # Подсчитываем частоту слов из файла
    for line in content:
        film_name = line.strip()  # Убираем символы перевода строки
        if film_name in film_count_from_file:
            film_count_from_file[film_name] += 1
        else:
            film_count_from_file[film_name] = 1


# Создаем список и сортируем его
items_list = []
for film, count in film_count_from_file.items():  # Используем данные из файла
    items_list.append((count, film))  # Помещаем количество первым

# Сортируем по убыванию количество (первый элемент кортежа)
items_list.sort(reverse=True)

# Есть еще другая сортировка:
# sorted_films = sorted(film_count.items(), key=lambda pair: pair[1], reverse=True)
# # 1. film_count.items() возвращает: dict_items([('Скала', 1), ('Западня', 3), ('Бэтман', 2)])
# # 2. key=lambda x: x[1] - сортировать по второму элементу каждой пары (по количеству)
# # 3. reverse=True - по убыванию

# Вывод
for film_count, film_name in items_list:
    print(f"'{film_name}' - {film_count}")

# 'Западня' - 3
# 'Бэтман' - 2
# 'Скала' - 1


value_1, value_2 = input(), input()
# I love Python
# Hello Python

with open('doc/file_1.txt', 'w', encoding='utf-8') as file_1:
    file_1.write(value_1)
with open('doc/file_2.txt', 'w', encoding='utf-8') as file_2:
    file_2.write(value_2)


with open('doc/file_1.txt', 'r') as file_1:
    content_1 = file_1.read()
    print(content_1)
    # I love Python
with open('doc/file_2.txt', 'r') as file_2:
    content_2 = file_2.read()
    print(content_2)
    # Hello Python


with open('doc/file_3.txt', 'w', encoding='utf-8') as file_3:
    file_3.write(f"{content_1}\n{content_2}")

with open('doc/file_3.txt', 'r') as file_3:
    content_3 = file_3.read()
    print(content_3)
    # I love Python
    # Hello Python