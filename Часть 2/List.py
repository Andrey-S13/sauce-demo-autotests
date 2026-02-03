films = input().split()

for film in films:
    if len(film) > 5:
        print(film)
# Вывести название фильмов больше 5 знаков


films = input().split()
count = 0

for film in films:
    if len(film) % 2 == 0:
        count += 1
print(count)
# Воин Джокер Дуэлянты Побег (вывести кол-во фильмов с четным числом символов)
# 3


films = input().split()
total = 0

for film in films:
    if film.isdigit():
        total += int(film)
        # print(total)
    if film.isalpha():
        total += len(film)
        # print(total)
print(total)
# Посчитать цифры и буквы вместе: Матрица 7 Скала 5 4 Схватка Бэтман = 41

files = input().split()

for file in files:
    if '.py' in file:
        print(file)
# Напечатать определенные элементы, которые содержат ".py"
# test.py cs.exe login_page.py python.txt


new_list = input().split()
count = 0

for i in new_list:
    if i.isdigit():
        continue
    count += 1
print(count)
# Вывести кол-во слов из текста: Матрица Два скала 5 10 Схватка 12 Бэтман
# 5


new_list = input()
new_list.split()
count = 0

for i in new_list:
    if i.isdigit() or i.isalpha():
        continue
    count += 1

print(count)
# Найти кол-во знаков: a!ds/w.3!0'\\@d1d
# 8


# Решение 1
new_list = input().split()
count = 0

for i in new_list:
    try:
        float(i)
        count +=1
    except:
        pass

print(count)
# Найти кол-во int и float цифр: яблоко 5 2.5 воин # 4
# 3

# Решение 2 - более утонченное
new_list = input().split()
count = 0

for i in new_list:
    i = i.replace('.','', 1)

    if i.isdigit():
        count += 1

print(count)


new_list = input().split()

for i in new_list:
    if i.isalpha():
        print(f'Я люблю {i}')
# Из списка составить фразу только со словами: банан сыр 1 чай #
# Я люблю банан
# Я люблю сыр
# Я люблю чай


# решение 1
numbers = list(map(int, input().split()))

max_count = 0  # 🕵️‍♂️ "Рекорд повторений" (пока 0)
most_frequent = None  # 🕵️‍♂️ "Подозреваемый" (пока никто)

for num in numbers:  # 🔍 Проверяем каждое число по очереди
    current_count = numbers.count(num)  # Подсчет улик (numbers.count(5) - сколько число "5" встречается в строке и т.д.)
    if current_count > max_count:  # Сравнение с рекордом
        most_frequent = num  # 🎯 Новый главный подозреваемый!
        max_count = current_count  # 🏆 Обновляем рекорд
print(most_frequent)  # 🎉 Выводим 5

# 5 8 2 1 3 5 4 5 2 8 12
# 5

# решение 2
numbers = list(map(int, input().split()))
max = 0

for el in numbers:
    if numbers.count(el) > max:
        max = numbers.count(el)
        max_el = el

print(max_el)