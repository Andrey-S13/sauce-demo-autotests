# # Любой тип данных, который мы выводим через input = integer
# var = input()
# print(type(var))
#
# # Если заранее объявить тип данных переменной, то вывыедется другой тип данных
# var = int(input())
# print(type(var))

var_1 = int(input())
var_2 = int(input())
result = var_1 + var_2
print(result)

var_3 = input()
var_4 = input()
result = var_3 + var_4
print("Меня зовут:" + var_3 + "" + var_4)

var_5 = input()
var_6 = input()
print(f"Меня зовут: {var_5} {var_6}")