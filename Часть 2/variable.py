var_1 = 10 # global variable (переменная)
var_2 = 20 # global variable (переменная)


# 1 действие: печать локальных переменных (будет: 10, 20), 2 действие: подсчет (будет: 70)
def summ():
    var_1 = 30 # Local variable
    var_2 = 40 # Local variable
    result = var_1 + var_2
    print(result)
print(var_1, var_2)
summ()

# Sub - subtraction (вычитание)
def sub():
    var_1 = 666 # Local variable
    var_2 = 333 # Local variable
    result = var_1 - var_2
    print(result)

sub()

# Использование смешанного типа переменных
def sub():
    var_2 = 9
    result = var_1 - var_2
    print(result)

sub()