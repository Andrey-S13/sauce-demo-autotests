# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

# Действие функции summ - это выводить на печать слово "hello"

# def summ(num_1, num_2):
#     result = num_1 + num_2
#     print(result)
# summ(10, 20)
# summ(30, 40)
# summ("Hello", " World")
# # В результате можно задать последовательность вывода переменных
# summ(num_2 = " Hello", num_1 = "World")

# def hi(name):
#     print("Hello" + name)
#
# hi(" Andrey")
#
# # OR
#
# def hi(name = " Andrey"):
#     print("Hello" + name)
#
# hi()
#
# # OR
#
# name = " Andrey"
# def hi(name):
#     print("Hello" + name)
#
# hi(name)

# name = input()
# def hi(name, age):
#     print("My name is " + name + " and i'm " + age)
#
# hi(name, "32")

name = "Andrey"
age = "29"
def hi(name, age):
    result = name + " " + age
    print(result)

hi(name, age)

# Если мы не хотим выводить нашу переменную на печать, но используем return и далее задаем переменную. Т.е. функцию def мы передаем в функцию print через переменную h1

name = "Andrey"
age = "29"
def hi(name, age):
    result = name + " " + age
    return result

h1 = hi(name, age)
print(h1)