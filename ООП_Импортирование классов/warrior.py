from base_person import Person


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

warrior = Warrior("Aragorn", 35, 185)
print(warrior.description_person())
# Aragorn, ему 35, его заряд ярости 100