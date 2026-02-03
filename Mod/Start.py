# import Modules
# import math
from Mod import math
from Mod import Some


Modules.some()
# hello world
print(math.acos(0.5))
print(dir(math))  # выводит все функции из модуля math
# 1.0471975511965979

import random
r = random.randrange(0, 10)
user = "user"
user_random = user + str(r)
print(user_random)
# user8

print(math.pi)

Some.mult(2, 6)
# Умножение переменных равно : 12