# a = 50
# b = int(input())
# result = a % b
# if result > 2:
#     print(result)
# elif result == 2:
#     print("Фыпа: " + str(result))
# else:
#     print("Конец: " + str(result))
# # 1) input 11 = 6
# # 2) input: 12 = "Фыпа: 2"
# # 3) input: 50 = "конец: 0"



def func():
    global_variable = 10
    print("Inside func(), global_variable is:", global_variable)

func()