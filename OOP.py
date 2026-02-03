class Person():
    """Создаем человека"""

    def __init__(self, name, age, height, weight):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def desctiption_person(self):
        """Получение опиcания человека"""
        description = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)  # конкатенация строк
        print(description)

    def get_weight(self):
        print("Вес нашего человека: " + str(self.weight) + " кг")

man = Person("Andrey", 30, 176, 90)
man.desctiption_person()
# Andrey, ему 30, его рост 176, его вес 90

man.get_weight()
# Вес нашего человека: 90 кг


"""
Создадим новый класс Animal без свойства (атрибута) weight

1 способ - указывать через экземпляр класса - через нужный атрибут weight
2 способ - создать новый метод изменения атрибута weight (более питоновский способ)
"""

class Animal():
    """Создаем животное"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты животного"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def desctiption_animal(self):
        """Получение опиcания животного"""
        description_animal = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)  # конкатенация строк
        print(description_animal)

    def get_weight_animal(self):
        """Получение веса животного"""
        print("Вес нашего животного: " + str(self.weight) + " кг")

    def update_weight_animal(self, kg):
        """ Изменение веса животного
        Способ 2 """
        self.weight = kg

animal = Animal("Cat", 9, 10)
animal.desctiption_animal()
# Cat, ему 9, его рост 10, его вес 100

'''Способ 1'''
animal.weight = 20
animal.get_weight_animal()
# Вес нашего животного: 20 кг

'''Способ 2'''
animal = Animal("Dog", 4, 40)
animal.update_weight_animal(30)
animal.desctiption_animal()
# Dog, ему 4, его рост 40, его вес 30



class Car():
    """Инициализируем атрибуты машины"""

    def __init__(self, color, model, country):
        self.color = color
        self.model = model
        self.country = country
        self.weight = 1200

    def description_car(self):
        """Получение описания машины"""
        description_car = ("Машина - " + self.model + ". Страна производитель " + self.country + ". Представлена в цвете: "
                           + self.color) + " и средней массой " + str(self.weight) + " (кг)"
        print(description_car)

    def change_weight(self, kg):
        """Изменение веса автомобиля"""
        self.weight = kg

car_1 = Car("red", "Toyota Corola", "Japan")
car_1.description_car()

# Машина - Toyota Corola. Страна производитель Japan. Представлена в цвете: red и средней массой 1200 (кг)

car_2 = Car("black", "Acura MDX", "USA")
car_2.change_weight(2000)
car_2.description_car()

# Машина - Acura MDX. Страна производитель USA. Представлена в цвете: black и средней массой 2000 (кг)


"""Наследование"""

class Warrior(Person):
    """Создаем класс Воин"""

    def __init__(self, name, age, height, weight):
        """Инициализируем атрибуты класса Воин"""
        super().__init__(name, age, height, weight)
        self.rage = 100  # новый атрибут у наследованного класса

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд  ярости равен: " + str(self.rage))

    def desctiption_person(self):
        """Переопределение метода Родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)  # конкатенация строк
        # print(description)
        return description

warrior = Warrior("Aragorn", 35, 185, 90)
warrior.desctiption_person()
# Aragorn, ему 35, его рост 185, его вес 90
warrior.get_rage()
# Заряд  ярости равен: 100


man.desctiption_person()
warrior.desctiption_person()
# Andrey, ему 30, его рост 176, его вес 90
# Aragorn, ему 35, его заряд ярости 100

print("Нового человека зовут: " + warrior.desctiption_person())  # Если в методе используется "return description"
# Нового человека зовут: Aragorn, ему 35, его заряд ярости 100



"""Урок наследование классов"""

class Alphabet:
    """Класс по созданию и работе с алфавитом"""
    def __init__(self, title, abbreviation, list_letters):
        self.title = title
        self.abbreviation = abbreviation
        self.list_letters = list_letters
        print("Новый алфавит создан")


    def description(self):
        """Получение описания алфавита"""
        description = (f"Название данного алфавита - {self.title}, его аббревиатура - {self.abbreviation},"
                       f" список букв - {self.list_letters}")
        print(description)


    def count_letter(self):
        """Количества букв в алфавите"""
        count = (len(self.list_letters))
        print(f"Количество букв в алфавите равно: {count}")



class Cyrillic(Alphabet):
    """Языки группы Кириллица"""

    def __init__(self, title, abbreviation, list_letters):
        super().__init__(title, abbreviation, list_letters)
        """Указываем какие атрибуты имеет Класс-наследник"""

serbian = Cyrillic("Сербский", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")
serbian.description()
serbian.count_letter()

# Новый алфавит создан
# Название данного алфавита - Сербский, его аббревиатура - SR, список букв - абвгдђежзијклмнњопрстћуфхцчџшыэ
# Количество букв в алфавите равно: 31




class Cyrillic(Alphabet):
    """Языки группы Кириллица"""

    def __init__(self, title, abbreviation, list_letters):
        super().__init__(title, abbreviation, list_letters)
        """Указываем какие атрибуты имеет Класс-наследник"""
        self.language_group = "Cyrl"

    def description(self):
        """Получение описания алфавита"""
        description = (f"Название данного алфавита - {self.title}, группа языков - {self.language_group},"
                          f"его аббревиатура - {self.abbreviation}, список букв - {self.list_letters}")
        print(description)

    def get_language_group(self):
        """Метод возвращающий аббревиатуру языковой группы"""
        print(f"Аббревиатура языковой группы {self.language_group}")
        return self.language_group


serbian = Cyrillic("Сербский", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")
serbian.description()
# Новый алфавит создан
# Название данного алфавита - Сербский, группа языков - Cyrl,его аббревиатура - SR, список букв - абвгдђежзијклмнњопрстћуфхцчџшыэ

russian = Alphabet("Русский", "RU", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
russian.description()
# Новый алфавит создан
# Название данного алфавита - Русский, его аббревиатура - RU, список букв - абвгдеёжзийклмнопрстуфхцчшщъыьэюя

serbian = Cyrillic("Сербский", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")
serbian.get_language_group()
# Новый алфавит создан
# Аббревиатура языковой группы Cyrl


"""Урок импортирование классов"""

