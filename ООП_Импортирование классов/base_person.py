class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age  # 30
        self.height = height
        self.weight = 100  # дефолтное значение

    def description_person(self):
        """Получение описания человека"""
        desctiption = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)
        print("Нового человека зовут: " + desctiption)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего челока: " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


man = Person("Andrey", 30, 100)
# man.description_person()
# Нового человека зовут: Andrey, ему 30, его рост 100, его вес 100




class Warrior(Person):
    """Создаем класс Воин"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса Воин"""
        super().__init__(name, age, height)
        self.rage = 100  # новый атрибут у наследованного класса

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд  ярости равен: " + str(self.rage))

    def description_person(self):
        """Переопределение метода Родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)  # конкатенация строк
        # print(description)
        return description