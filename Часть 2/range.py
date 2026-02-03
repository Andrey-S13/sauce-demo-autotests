# Range: start, stop, step

# range(0, 10, 2)
r = range(10)
print(r)
# (0, 10)

r = list(range(0, 10))
print(r)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = list(range(2, 10))
print(r)
# [2, 3, 4, 5, 6, 7, 8, 9]

r = list(range(0, 11, 2))
print(r)
# [0, 2, 4, 6, 8, 10]

# list = (0, 1, 2, 3)
for f in range(4):
    print(f)
# 0 1 2 3


a = int(input())

for i in range(1, a+1):
    print(i**2)
# Вывести от 1 до X квадраты чисел