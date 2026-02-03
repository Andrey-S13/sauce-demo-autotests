# Список сотрудников - файл
# загрузить файл и работь со списком
# или список сохранить в наш

# fw = open('doc/file.txt', 'a')
# fw.write("hello world\n")
# fw.close()
#   'doc/file.txt' - в папке "doc" создается файл "file.txt"
#   выполняется действие 'a' = запись новой строки в конец документа
#   fw.write - указываем наше действие, т.е. записываем строку "hello world"
#   \n - переносит текст на другую строку
#   fw.close() - закрываем наш документ


# var = input("Write something: ")
# fw = open('doc/file.txt', 'a')
# fw.write(var)
# fw.close()

#   a – запись новых данных в файл и помещение их в конец файла
#   w – запись новых данных с удалением старых данных
#   r - чтение записи

# fw = open('doc/file_2.txt', 'w')
# fw.write('write again\n')
# fw.close()

# fr = open('doc/file.txt', 'r')
# text = fr.read()
# fr.close()
#   переменная text, которая будет хранить содержимое нашего файла
#
# print(text)

# with open("doc/file.txt", "r") as file:
#     content = file.read()
#     print(content)

# var = input("Напиши что-нибудь: ")
# fw = open("doc/file.txt", "a")
# fw.write(var + "\n")
# fw.close()

#   \n - это символьная последовательность (управляющий символ), чтобы в файл добавлялась информация с новой строки

# for i in range(3):
#     doc_file = open('doc/file.txt', 'a')
#     doc_file.write("Это тестовый текст N" + str(i + 1) + "\n")
#     doc_file.close()

# doc_file = open('doc/file.txt', 'r')
# text = doc_file.read()
# doc_file.close()

# print(text)


# fw = open('doc/file.txt', 'w', encoding='utf-8')
# var = input("Замени приветствие на новом языке: ")
# fw.write(var)
# print(var)
#
# fw.close()


# fr = open('doc/file.txt', 'а', encoding='utf-8')
# name_1 = input()
# name_2 = input()
# f = '{} {}'
# var_2 = f.format(name_1, name_2)
# fr.write("\n" + var_2)
# print("Введи дополнительное приветствие: " + var_2)
# fr.close()


fr = open('doc/file.txt', 'r+', encoding='utf-8')
text = fr.read()
print("Текущий текст: " + text)
print("Введите новый текст: ")
new_text = input()
fr.write("\n" + new_text)
print("Новый текст:" + new_text)
fr.close()


value_1 = input()

fw = open("doc/file_4.txt", 'w')
fw.write(value_1)
fw.close()

fr = open("doc/file_4.txt", 'r')
text = fr.read()
print(text)


value_1 = input()
value_2 = input()

fw = open('doc/file.txt', 'w')
fw.write(f'{value_1}\n{value_2}')
fw.close()

fr = open('doc/file.txt', 'r')
print(fr.read())
fr.close()
# Создайте в коде файл с именем file.txt, запишите в него сперва первое значение, затем с новой строки второе значение. Выведите на печать содержимое файла построчно
# I love Python
# I love QA
# I love Python
# I love QA


films = input().split()

fw = open('doc/Files.txt', 'w')
for i in films:
    fw.write(f'{i}\n')
fw.close()

fr = open('doc/Files.txt', 'r')
elements = fr.read()
print(f'Список фильмов: \n{elements}')
count = len(films)
print(f'Общее кол-во фильмов: \n{count}')

# Матрица Скала Схватка Бэтман
# 4


value_1 = input()

# Добавляем инфу в фалй 1
fw = open('doc/file_1.txt', 'w')
fw.write(value_1)
fw.close()
# Читаем инфу из фалйа 1
fr = open('doc/file_1.txt', 'r')
text_1 = fr.read()
fr.close()
# Копируем инфу из фалйа 1 в файл 2
fw = open('doc/file_2.txt', 'w')
fw.write(text_1)
fw.close()
# Читаем инфу из фалйа 2
fr = open('doc/file_2.txt', 'r')
text_2 = fr.read()
print(text_2)
fr.close()

# I love Python


films = input().split()
value_1 = input()

fw = open('doc/file_1.txt', 'w')
for i in films:
    fw.write(f"{i}\n")
fw.close()

fr = open('doc/file_1.txt', 'r')
line = fr.readlines()
line_value = line[int(value_1) - 1].strip()
print(line_value)
fr.close()

# Матрица Скала Схватка Бэтман
# 2
# Скала


films = input().split()
value_1 = input()

fw = open('doc/file_1.txt', 'w')
for i in films:
    fw.write(f"{i}\n")  # можно еще fw.write(i.strip() + '\n') - strip() - удаляет пробелы у строки в начале и в конце
fw.close()

fr = open('doc/file_1.txt', 'r')
line = fr.readlines()
for i in range(len(films)):
    if films[i] == value_1:
        print(i+1)
fr.close()

# Матрица Скала Схватка Бэтман
# Скала
# 2


films = input().split()

fw = open('doc/file_1.txt', 'w')
for i in range(len(films)):
    fw.write(films[i].strip() + '\n')
    if i < len(films)-1:  # Добавляем звездочки после каждого фильма, кроме последнего
        fw.write('*'*5 + '\n')
fw.close()

fr = open('doc/file_1.txt', 'r')
line = fr.read()
print(line)
fr.close()

# Матрица Скала Схватка Бэтман

# Матрица
# *****
# Скала
# *****
# Схватка
# *****
# Бэтман
