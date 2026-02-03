data = {'a': 10, 'b': 20, 'c': 15}

result = max(data.items(), key = lambda value : value[1])
print(*result, sep=' - ')  # если не поставить *, то будет ответ в виде ('b', 20). *result - распаковывает кортеж
# на отдельные аргументы
'''
lambda v: v[1] - это анонимная функция
Лямбда-функция эквивалентна:
def get_value(pair):
    return pair[1]
    
для кортежа ('a', 10):
v[0] = 'a' (key)
v[1] = 10 (value)
'''

# b - 20