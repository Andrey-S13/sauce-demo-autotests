def var():

    a = float(input())
    b = int(input())
    c = int(input())

    var_x = a**2 + b**2 + c
    var_y = 2*c + a * b
    var = var_x + var_y

    return var

print(round(var()))

