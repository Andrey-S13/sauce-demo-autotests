str_1 = "hello"
print(str_1)
print(dir(str_1))

# Все буквы верхнего регистра
print(str_1.upper())

# Только первая буква верхнего регистра
print((str_1.title()))

# Все символы в нижнем регистре
str_2 = "WORLD"
print(str_2.lower())

# Код читается сверху вниз. И name = Ivan уже не видно
name = 'Ivan'
name = 'Anna', 'Ivan', 'Andrey'
a = "Hello {}"
result = a.format(name)
print(result)

# Переменная "a" может содержать два значения через фигурные скобки
first_name = 'Andrey'
last_name = 'Savin'
a = '{} {}'
result = a.format(first_name, last_name)
print("Меня зовут : " + result)

# formatted string (F-srting)- данная конструкция экономит место
result = f'{first_name} {last_name}'
print("Меня зовут: " + result)

# Меня зовут Alex, мне 30 лет
name = "Alex"
age = 30
print("Меня зовут " + name + ", мне " + str(age) + " лет")
print(f"Меня зовут {name}, мне {age} лет")

# Сумма чисел равна 15
num_1 = 5
num_2 = 10
print(f"Cумма числ равна {num_1 + num_2}")