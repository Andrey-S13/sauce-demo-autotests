# # num_1 = 5
# # num_2 = 15
# # result = num_1/num_2
# # print("Answer is: " + str((round(result, 2))))
#
# name = "Andrey"
# surname = "Suvorov"
# last_name = "Dmitrievich"
# a = "{} {} {}"
# result = a.format(name, surname, last_name)
# print(result) # Andrey Suvorov Dmitrievich
#
# name = "A"
# surname = "S"
# last_name = "D"
# result = f'{name}{surname}{last_name}'
# print(result) # ASD

# cars = ['Toyota', 'Mitsubishi', 'Subaru', 'Honda', 'Nissan']
# for c in cars:
#     if c == 'Toyota':
#         print(" Toyota Corolla")
#     else:
#         print(" not found")
#         if c == 'Mitsubishi':
#             print(" Mitsubishi Mirage")
#         else:
#             print(" khm...")

materials = ["бетон", "дерево", "металл"]
for element in materials:
    print(element)

count = 0
while count < 5:
    count = count + 1
    #  более компактная запись: count += 1
    print("Значение count: ", count)

print("Цикл завершен.")

