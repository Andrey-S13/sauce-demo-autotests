file_name = 'Mod/math.py'
data = 'pi = 5'
# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'w') as var:
    var.write(data)

import math
print(math.pi)
#3.141592653589793

from Mod import math
print(math.pi)
#5

file_name_2 = 'Mod/Some.py'
data_2 = '123'
with open(file_name_2, 'a') as var_2:
     var_2.write(data_2)

from Mod import Some
Some.sub(10, 5)
#Разность переменных равна : 5
Some.sum(10, 5)
#Сумма переменных равна : 15