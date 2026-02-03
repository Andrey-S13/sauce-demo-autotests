personal = ["Alex", "Ivan", "Nasty", "Olga"]
#             0        1       2        3
result = personal[0] + " " + personal[2]
print(result + " - the best friends")
# Вывод: Alex Nasty - the best friends


number = ["1", "5", "23", "44"]
#          0    1    2     3
print(number[2])
# Вывод:23



number = [1, 5, 23, 44]
result_num = number[1] + number[3]
print(result_num)
# Вывод:49



# В переменной можно сохранять ссылки на некоторые объекты
number = [1, 5, 23, 44]
#         0  1   2   3
num_2 = number[1]
# Значение и тип данных из нашего списка (объекта) мы выводим в печать через переменную "num_2"
print(num_2)
# Вывод:5


# Если у нас большой список и мы не знаем, сколько в нем объектов можно использовать функцию len. Равно 4 объекта.
print(len(personal))
# Вывод: 4

# Обращение к последнему объекту
print(personal[-1])
# Вывод: Olga

# Вывести диапазон объектов из списка. Обратиь внимание на последний из поиска индекс. Он записывается как +1. В нашем примере Nasty имеет индекс 2, но для поиска записываем 3.
print(personal[0:3])
# Вывод: ['Alex', 'Ivan', 'Nasty']

# Обратиться с какого-то элемента и до конца списка
print(personal[1:])
# Вывод: ['Ivan', 'Nasty', 'Olga']

# Добавить в список новый объект
personal.append("Fedor")
print(personal)
# Вывод: ['Alex', 'Ivan', 'Nasty', 'Olga', 'Fedor']

number = [1, 5, 23, 44]
personal = ["Alex", "Ivan", "Nasty", "Olga"]
pn = []
pn.append(personal)
pn.append(number)
print(pn)
# Вывод: [['Alex', 'Ivan', 'Nasty', 'Olga'], [1, 5, 23, 44]]



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12 , 13, 14, 15]
#         0. 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11,  12, 13, 14

print(number) # Выводим весь список [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number[:5]) # from 0 to 4 [1, 2, 3, 4, 5]
print(number[5:]) # from 5 to end [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(number[5:10]) # from 5 to 9 [6, 7, 8, 9, 10]
print(number[::5]) # increment|приращение 5 [1, 6, 11]
print(number[1::3]) # from 1 with increment 3 [2. 5, 8, 11, 14]
print(number[:-4]) # whole list within the last 4 numbers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(number[1:-1]) # without first and last [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(number[::-1]) # reverse list|реверс [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(number[::-2]) # reverse list with increment 2 [15, 13, 11, 9, 7, 5, 3, 1]
print(number[-2::-2]) # reverse list from 2 and increment 2 [14, 12, 10, 8, 6, 4, 2]
print(number[10::-4]) # reverse list from 10 and increment 4 [11, 7, 3]

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Получаем числовое значение от пользователя и преобразуем его в int
user_input = int(input("Введите число: "))

# Выполняем вычисления
res = (user_input + number[9]) / number[14]

# Выводим введенное пользователем значение
print("Введенное число:", user_input)

# Сравниваем результат с 1 и 10
if 1 < res < 10:
    print("Результат в диапазоне от 1 до 10:", res)
     #        elif pes < 1:
     #            print(res + " Число меньше 1")