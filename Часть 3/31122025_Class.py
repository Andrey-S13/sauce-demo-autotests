'''
ооп - методология, основанная на представлении программы в виде совокупности объектов, каждый из которых является экземпляром
определенного класса, а классы образуют иерархию наследования

класс - выступает чертежом для объекта (как иструкция).

класс = машина
объект = Тойота
'''

# class Person():
#     """Модель человека"""
#
#     def __init__(self, name, age):
#         """Инициализация атрибутов человека - имя, возраст"""
#         self.name = name
#         self.age = age
#         print("Человек создан")
#
#     def sing(self):  # ссылка на экземпляр класса Person
#         """Просим человека спеть"""
#         print(self.name + " поет")
#     def dance(self):
#         """Просим человека станцевать"""
#         print(self.name + " танцует")
#
# """Создаем объкт man"""
# man = Person("Andrey", 30)
# """хранится экземпляр класса Person с указанием атрибутов, которые мы получаем"""
# print(man.name)
#
# """Используем метод для нашего объекта"""
# man.dance()
#
# woman = Person("Olga", 25)
# woman.sing()

# Человек создан - 1
# Andrey
# Andrey танцует
# Человек создан - 2
# Olga поет



class Students():
    """Создание класса Студенты"""
    def __init__(self, num, FIO, group):
        self.num = num
        self.FIO = FIO
        self.group = group
        print("Студент зачислен")

    def change_group_by_num(self, num):
        if num > 15:
            self.group = 2

    def __str__(self):
        return f"{self.FIO} {self.num} {self.group}"

student = Students(1, 'Суворов Андрей Дмитриевич', 1)
# print(student)

student.change_group_by_num(20)
print(student.group)

print(student)

# Студент зачислен
# Суворов Андрей Дмитриевич 1 1
# 2
# Суворов Андрей Дмитриевич 1 2