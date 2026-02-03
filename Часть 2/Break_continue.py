list = [1, 4, 6, 10, 12]

for i in list:
    print(i) # 1 4 6 10 12 - обратились к каждому элементу списка и по очереди вывели его на печать

list = [1, 4, 6, 10, 12]
for i in list:
    if i == 6:
        print("Ура 6!")
        break
    print(i) # 1 4 Ура 6! Но функция print(i) будет уже недоступна


# Имитация формы авторизации: логин/пароль
login = input("Type your login: ")

while True:
    if login == "Andrey":
        print("Your login is true")
        password = input("Type your password")
    else:
        print("Your login is false")
        break


list = [1, 4, 6, 8, 10, 12]

for i in list:
    if i == 10:
        print("Плохо 10!")
        break
    if i == 4:
        print("Ура, 4!")
    if i == 6:
        print("Ура 6!")
        continue
    print(i)

    # 1
    # Ура, 4!
    # 4
    # Ура 6!
    # 8
    # Плохо 10!


numbers = list(map(int, input().split()))
index = 0

while True:
    if numbers[index] < 0:
        print(numbers[index])
        break
    index += 1
    continue
# вывести первое отрицательное число из списка


numbers = list(map(int, input().split()))
index = 0

while index < len(numbers):
    if numbers[index] % 2 != 0:
        print(numbers[index])
    index += 1
    continue
# Вывести из списка нечетные числа


numbers = list(map(int, input().split()))
index = 0
positive = 0
negative = 0

while index < len(numbers):

    if numbers[index] > 0:
        # print(numbers[index])
        positive += 1
        index += 1
        continue  # Считаем все положительные, далее нижний блок
    if numbers[index] < 0:
        # print(numbers[index])
        negative += 1
        index += 1 # Когда нижний блок досчитал числа - остановка программы
    break  # Если условие число = 0 или верхние блоки закончились, то выполняется отсановка программы
print(positive)
print(negative)
# Из списка вывести сначала положительные числа, затем отрицательные


numbers = list(map(int, input().split()))

for number in numbers:
    if number % 3 != 0 and number % 5 !=0:
        continue
    print(number)
# 10 5 7 3 8 15 - найти кратные 3 и 5:
# 10
# 5
# 3
# 15

# Решение 1
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)  # список начинается от большего к меньшему

for i in range(1, len(numbers)):
    if numbers[i] < numbers[0]:
        print(numbers[i])
        break
# второе по величине число в списке, используя оператор break.
# 10 5 7 3 8 15
# 10

# Решение 2
numbers = list(map(int, input().split()))  # Вводим список из цифр
max_num = max(numbers)  # В списке находим максимальное число
my_num = 0  # Создаём переменную, в которою будем сохранять нужное число

for i in numbers:  # Начинаем перебирать элементы списка
    if i == max_num:  # Если наткнулись на максимальное число, то пропускаем
        continue
    elif i < max_num:  # Если текущий элемент списка меньше максимального числа
        if i > my_num:  # то проверяем, больше ли он текущего значения нашей переменной
            my_num = i  # Если больше, то сохраняем текущее значение в нашу переменную
        else:
            continue

print(my_num)


numbers = list(map(int, input().split()))

for i in numbers:
    if i < 0:
        continue
    print(i)
# Вывести из списка положительные числа


# Решение 1 через for
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
    if i < 0:
        continue
    count += i

print(count)

# Вывести сумму положительных числел
# 10 -5 7 -3 8 -1
# 25

# Решение 2 через break
numbers = list(map(int, input().split()))
count = 0

for i in numbers:
    while i > 0:
        count += i
        break

print(count)