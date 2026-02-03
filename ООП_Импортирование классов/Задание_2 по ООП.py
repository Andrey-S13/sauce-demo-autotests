""" Инструкции к заданию:
Создайте класс Car. Добавьте обязательные атрибуты класса: модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4.
Создайте 1 экземпляр класса
Создать класс наследник - Грузовик. Который, наследует все атрибуты класса, но количество колес = 8.
Создать 1 экземпляр класса Наследника
Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description) """

class Car():
    """Создание класса Машина"""

    def __init__(self, model, year_of_manufacture, engine_capacity, price, mileage):
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = 4

    def description(self):
        """Получение описания машины"""
        description = (f"Данная модель '{self.model}' c {self.number_of_wheels} колесами была выпущена в "
                       f"{self.year_of_manufacture} году и имеет объем двигателя {self.engine_capacity}л. "
                       f"Автомобиль с пробегом {self.mileage} продается по цене {self.price}р")
        print(description)

# Создаем объект Машина (экземпляр класса)
car_1 = Car("Mercedes-Benz ML 350", 2008, 3.5, 1_100_000, 300_000)
car_1.description()


class Truck(Car):
    """Создание класса Грузовик"""

    def __init__(self, model, year_of_manufacture, engine_capacity, price, mileage):
        super().__init__(model, year_of_manufacture, engine_capacity, price, mileage)
        self.number_of_wheels = 8

# Создаем объект Грузовик (экземпляр класса)
truck_1 = Truck("Volvo FM 8x4", 2006, 10.8, 3_200_000, 700_000)
truck_1.description()
