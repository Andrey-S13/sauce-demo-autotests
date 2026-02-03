# age = 25
# name = "Andrey"
# if age == 25 and name == "Andrey":
#     print("Мне 25 лет и меня зовут Andrey")
# elif age > 25:
#     print("Мне больше 25 лет")
# else:
#     print("Мне меньше 25 лет")

# age = 20
# name = "Andre"
# if age == 25 or name == "Andrey":
#     print("Мне 25 лет и меня зовут Andrey")
# else:
#     print("Мне меньше 25 лет")

# name = "Andrey"
# if "И" in name == "Andrey":
#     print("Меня зовут Андрей")
# else:
#     print("Меня не зовут Андрей")

pin = 1234
print("Введите пожалуйста Ваш пин-код")
user_pin = int(input())

if pin == user_pin:
    print("Какую сумму вы хотите снять?")
else:
    print("Ошибка, введите корректный пин-код, у Вас осталось 2 попытки")
    user_pin = int(input())
    if pin == user_pin:
        print("Какую сумму вы хотите снять?")
    else:
        print("Ошибка, введите корректный пин-код, у Вас осталась 1 попытка")
        user_pin = int(input())
        if pin == user_pin:
            print("Какую сумму вы хотите снять?")
        else:
            print("Ошибка, Ваша карта заблокирована. Пожалуйста, обратитесь в банк")

num_1 = 3
if num_1>0:
    print('The number is more than 0: ' + num_1)
print('this phrase print always')