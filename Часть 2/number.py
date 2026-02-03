# num_1 = 5
# print(type(num_1))
num_1 = -5
num_2 = 10
text_1 = 'Сумма'
result = -(num_2 + num_1)
print(result)

num_1 = 5
num_2 = 10
result = -(num_2-num_1)*(num_2+num_1)
print((result))

num_1 = 5
num_2 = 10
result = -(num_2-num_1)*(num_2+num_1)
print((result*0.1))

# ** - возведение в степень
num_3 = num_1**2
print((num_3))

# результат 0.2
num_1 = 15
num_2 = 10
result = num_1 / num_2
print(result)

# int выведет целое число в print. Результат округления = 0
num_1 = 15
num_2 = 10
result = num_1 / num_2
print(int(result))

# int заменяем // и = также целостное число. Результат также = 0
num_1 = 15
num_2 = 10
result = num_1 // num_2
print(int(result))

num_4 = 50
num_5 = 8
result = num_4 / num_5
print(int(result))

# Останочное от деления . Результат остатка = 2. Т.к. 6 * 8 = 48. 50 - 48 = остаток 2
num_4 = 50
num_5 = 8
result = num_4 % num_5
print(int(result))

# == приравнивание
num_4 = 50
num_5 = 8
result = num_4 % num_5
print(num_1 >= num_2)

# round - округление
print(round(10/3))

# Запятая после означает, до какого знака округляем после запятой. В данном случае = 3.33
print(round(10/3, 2))

# int позволяет вывести второй результат с округделием до целого вне зависимости, что оно включает. Т.е. вместо 20.5 получилось 20
num_1 = float(10.5)
print(num_1)
num_2 = 10
result = num_1 + num_2
print(int(result))

# int - округление до целого Т.е. 10.5 + 10.5 = 21, выводится целое
num_1 = float(10.5)
print(num_1)
num_2 = 10.5
result = num_1 + num_2
print(int(result))
